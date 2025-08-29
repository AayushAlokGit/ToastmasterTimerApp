"""
Timer functionality for the Toastmaster Timer App
"""

import time
import threading
from typing import Optional, Callable
from .speech_types import SpeechType, TimerColor, SpeechConfig
from .display_manager import DisplayManager


class TimerEngine:
    """Core timer functionality with threading support"""
    
    def __init__(self):
        self.current_speech_type: Optional[SpeechType] = None
        self.timer_running = False
        self.start_time: Optional[float] = None
        self.current_color = TimerColor.BLANK
        self.timer_thread: Optional[threading.Thread] = None
        self.grace_period_started = False
        self.grace_period_ended = False
        self.on_timer_update: Optional[Callable] = None
    
    def set_timer_update_callback(self, callback: Callable):
        """Set callback function to be called on timer updates"""
        self.on_timer_update = callback
    
    def start_timer(self, speech_type: SpeechType):
        """Start timing for specified speech type"""
        self.current_speech_type = speech_type
        self.timer_running = True
        self.grace_period_started = False
        self.grace_period_ended = False
        self.current_color = TimerColor.BLANK
        DisplayManager.set_background_color(TimerColor.BLANK)
        
        config = SpeechConfig.get_config(speech_type)
        print(f"\nStarting timer for {config['name']}...")
        print("Timer will begin in 3 seconds...")
        time.sleep(3)
        
        self.timer_thread = threading.Thread(target=self._timer_worker)
        self.timer_thread.daemon = True
        self.timer_thread.start()
    
    def stop_timer(self) -> int:
        """Stop the current timer and return elapsed time"""
        if self.timer_running:
            self.timer_running = False
            elapsed = int(time.time() - self.start_time) if self.start_time else 0
            
            # Reset terminal colors
            DisplayManager.set_background_color(TimerColor.BLANK)
            DisplayManager.clear_screen()
            
            return elapsed
        return 0
    
    def get_elapsed_time(self) -> int:
        """Get current elapsed time in seconds"""
        if self.start_time:
            return int(time.time() - self.start_time)
        return 0
    
    def is_running(self) -> bool:
        """Check if timer is currently running"""
        return self.timer_running
    
    def get_current_speech_type(self) -> Optional[SpeechType]:
        """Get currently selected speech type"""
        return self.current_speech_type
    
    def get_current_color(self) -> TimerColor:
        """Get current timer color"""
        return self.current_color
    
    def _timer_worker(self):
        """Background timer worker thread"""
        if not self.current_speech_type:
            return
            
        config = SpeechConfig.get_config(self.current_speech_type)
        self.start_time = time.time()
        
        while self.timer_running:
            elapsed = int(time.time() - self.start_time)
            
            # Determine current color based on elapsed time
            current_color = TimerColor.BLANK
            for timing_seconds, color in config['timings']:
                if elapsed >= timing_seconds:
                    current_color = color
            
            # Update color if changed
            if current_color != self.current_color:
                self.current_color = current_color
                DisplayManager.set_background_color(current_color)
            
            # Handle grace period notifications
            self._handle_grace_period_notifications(elapsed, config)
            
            # Display timer info
            DisplayManager.show_timer_info(self.current_speech_type, elapsed, self.current_color)
            
            # Call update callback if set
            if self.on_timer_update:
                self.on_timer_update(elapsed, self.current_color)
            
            time.sleep(1)
    
    def _handle_grace_period_notifications(self, elapsed: int, config: dict):
        """Handle grace period start/end notifications"""
        grace_period = config.get('grace_period', 0)
        if grace_period <= 0:
            return
        
        red_time = SpeechConfig.get_red_time(self.current_speech_type)
        grace_end_time = SpeechConfig.get_grace_end_time(self.current_speech_type)
        
        # Check if grace period just started
        if elapsed >= red_time and not self.grace_period_started:
            self.grace_period_started = True
            DisplayManager.show_grace_period_notification("started", grace_period)
            time.sleep(2)  # Show notification for 2 seconds
        
        # Check if grace period just ended
        if elapsed >= grace_end_time and not self.grace_period_ended:
            self.grace_period_ended = True
            DisplayManager.show_grace_period_notification("ended")
            time.sleep(2)  # Show notification for 2 seconds


class TimerController:
    """High-level timer controller that coordinates timer engine with other components"""
    
    def __init__(self):
        self.engine = TimerEngine()
    
    def start_speech_timer(self, speech_type: SpeechType) -> bool:
        """Start a timer for a specific speech type"""
        try:
            self.engine.start_timer(speech_type)
            return True
        except Exception as e:
            print(f"Error starting timer: {e}")
            return False
    
    def stop_speech_timer(self) -> int:
        """Stop the current timer and return elapsed time"""
        return self.engine.stop_timer()
    
    def is_timer_running(self) -> bool:
        """Check if timer is currently running"""
        return self.engine.is_running()
    
    def get_timer_status(self) -> dict:
        """Get current timer status information"""
        return {
            "running": self.engine.is_running(),
            "speech_type": self.engine.get_current_speech_type(),
            "elapsed_time": self.engine.get_elapsed_time(),
            "current_color": self.engine.get_current_color(),
            "grace_period_started": self.engine.grace_period_started,
            "grace_period_ended": self.engine.grace_period_ended
        }
    
    def wait_for_timer_completion(self):
        """Wait for timer to complete (until stopped by user)"""
        while self.engine.is_running():
            time.sleep(0.1)
