"""
Display utilities for the Toastmaster Timer App
"""

import os
from speech_types import SpeechType, TimerColor, SpeechConfig


class DisplayManager:
    """Handles all display-related functionality"""
    
    @staticmethod
    def clear_screen():
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def set_background_color(color: TimerColor):
        """Set terminal background color based on Windows PowerShell"""
        if color == TimerColor.BLANK:
            # Reset to default colors
            os.system('color')
        elif color == TimerColor.GREEN:
            # Black text on green background
            os.system('color 02')
        elif color == TimerColor.YELLOW:
            # Black text on yellow background  
            os.system('color 06')
        elif color == TimerColor.RED:
            # White text on red background
            os.system('color 04')
    
    @staticmethod
    def show_main_menu():
        """Display the main menu"""
        DisplayManager.clear_screen()
        print(f"\n{'='*60}")
        print("  🎤 TOASTMASTER TIMER APPLICATION 🎤")
        print(f"{'='*60}")
        print("\nSelect Speech Type:")
        print("1. Ice Breaker Speech (4-6 minutes)")
        print("2. Usual Speech (5-7 minutes)")  
        print("3. Speech Evaluation (2-3 minutes)")
        print("4. Table Topic Speech (1-2 minutes)")
        print("5. Test Speech (Color changes every 30s)")
        print("6. View Speech Records")
        print("7. Exit")
        print(f"\n{'='*60}")
    
    @staticmethod
    def show_timer_info(speech_type: SpeechType, elapsed_seconds: int, current_color: TimerColor):
        """Display current timer information"""
        DisplayManager.clear_screen()
        
        config = SpeechConfig.get_config(speech_type)
        if not config:
            return
            
        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60
        
        print(f"\n{'='*60}")
        print(f"  TOASTMASTER TIMER - {config['name'].upper()}")
        print(f"  Expected Duration: {config['duration_range']}")
        print(f"{'='*60}")
        print(f"\n  ELAPSED TIME: {minutes:02d}:{seconds:02d}")
        print(f"  CURRENT SIGNAL: {current_color.value.upper() if current_color != TimerColor.BLANK else 'BLANK'}")
        
        # Show grace period status if applicable
        grace_period = config.get('grace_period', 0)
        if grace_period > 0:
            red_time = SpeechConfig.get_red_time(speech_type)
            grace_end_time = SpeechConfig.get_grace_end_time(speech_type)
            
            if elapsed_seconds >= grace_end_time:
                print(f"  ⚠️  GRACE PERIOD OVER - DISQUALIFIED!")
            elif elapsed_seconds >= red_time:
                remaining_grace = grace_end_time - elapsed_seconds
                print(f"  🟠 GRACE PERIOD ACTIVE - {remaining_grace}s remaining")
        
        # Show timing breakdown
        print(f"\n  TIMING SIGNALS:")
        for timing_seconds, color in config['timings']:
            timing_min = timing_seconds // 60
            timing_sec = timing_seconds % 60
            status = "✓" if elapsed_seconds >= timing_seconds else " "
            print(f"  {status} {timing_min:02d}:{timing_sec:02d} - {color.value.upper()}")
        
        # Show grace period details if applicable
        if grace_period > 0:
            red_time = SpeechConfig.get_red_time(speech_type)
            grace_start_min = red_time // 60
            grace_start_sec = red_time % 60
            grace_end_time = SpeechConfig.get_grace_end_time(speech_type)
            grace_end_min = grace_end_time // 60
            grace_end_sec = grace_end_time % 60
            
            # Show grace period timing
            if elapsed_seconds >= red_time:
                grace_status = "🟠" if elapsed_seconds < grace_end_time else "⚠️"
            else:
                grace_status = " "
            print(f"  {grace_status} {grace_start_min:02d}:{grace_start_sec:02d}-{grace_end_min:02d}:{grace_end_sec:02d} - GRACE PERIOD ({grace_period}s)")
            
            disqualify_status = "⚠️" if elapsed_seconds >= grace_end_time else " "
            print(f"  {disqualify_status} {grace_end_min:02d}:{grace_end_sec:02d} - DISQUALIFIED (Grace period exceeded)")
        
        print(f"\n{'='*60}")
        print("  Press Ctrl+C to stop timer and record speech")
        print(f"{'='*60}")
    
    @staticmethod
    def show_grace_period_notification(notification_type: str, grace_period: int = 0):
        """Show grace period start/end notifications"""
        DisplayManager.clear_screen()
        print(f"\n{'='*60}")
        
        if notification_type == "started":
            print(f"  🟠 GRACE PERIOD STARTED!")
            print(f"  Speaker has {grace_period} seconds to conclude")
        elif notification_type == "ended":
            print(f"  ⚠️  GRACE PERIOD OVER!")
            print(f"  Speaker is now DISQUALIFIED in competitions")
        
        print(f"{'='*60}")
    
    @staticmethod
    def show_speech_recorded(speaker_name: str, speech_name: str, duration_formatted: str):
        """Show speech recorded confirmation"""
        print(f"\n✓ Speech recorded:")
        print(f"  Speaker: {speaker_name}")
        print(f"  Type: {speech_name}")
        print(f"  Duration: {duration_formatted}")
    
    @staticmethod
    def show_welcome_message():
        """Show welcome message"""
        print("Welcome to Toastmaster Timer App!")
    
    @staticmethod
    def show_goodbye_message():
        """Show goodbye message"""
        print("\nThank you for using Toastmaster Timer App!")
    
    @staticmethod
    def show_error_message(message: str):
        """Show error message"""
        print(f"\nError: {message}")
    
    @staticmethod
    def show_invalid_choice():
        """Show invalid choice message"""
        print("Invalid choice. Please try again.")
