#!/usr/bin/env python3
"""
Toastmaster Timer App - Main Application
A console application that provides visual timing feedback for Toastmaster speeches
by changing terminal background colors (green, yellow, red) at specified intervals.
"""

import time
from typing import Dict
from speech_types import SpeechType, SpeechConfig
from timer_engine import TimerController
from record_manager import RecordManager
from display_manager import DisplayManager


class ToastmasterTimerApp:
    """Main application class that coordinates all components"""
    
    def __init__(self):
        self.timer_controller = TimerController()
        self.record_manager = RecordManager()
        self.speech_type_map = {
            '1': SpeechType.ICE_BREAKER,
            '2': SpeechType.USUAL_SPEECH,
            '3': SpeechType.EVALUATION,
            '4': SpeechType.TABLE_TOPIC,
            '5': SpeechType.TEST
        }
    
    def run(self):
        """Main application loop"""
        DisplayManager.show_welcome_message()
        
        while True:
            try:
                self._show_menu_and_handle_choice()
                    
            except KeyboardInterrupt:
                self._handle_keyboard_interrupt()
                break
            except Exception as e:
                DisplayManager.show_error_message(str(e))
                input("Press Enter to continue...")
    
    def _show_menu_and_handle_choice(self):
        """Show menu and handle user choice"""
        DisplayManager.show_main_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice in self.speech_type_map:
            self._handle_speech_selection(choice)
        elif choice == '6':
            self._handle_view_records()
        elif choice == '7':
            self._handle_exit()
            return False
        else:
            self._handle_invalid_choice()
        
        return True
    
    def _handle_speech_selection(self, choice: str):
        """Handle speech type selection and timer execution"""
        speech_type = self.speech_type_map[choice]
        config = SpeechConfig.get_config(speech_type)
        
        print(f"\nSelected: {config['name']} ({config['duration_range']})")
        confirm = input("Press Enter to start timer or 'q' to go back: ").strip()
        
        if confirm.lower() != 'q':
            self._run_speech_timer(speech_type, config)
    
    def _run_speech_timer(self, speech_type: SpeechType, config: Dict):
        """Run the timer for a specific speech type"""
        try:
            if not self.timer_controller.start_speech_timer(speech_type):
                print("Failed to start timer")
                return
            
            # Wait for timer to complete or be interrupted
            self.timer_controller.wait_for_timer_completion()
                
        except KeyboardInterrupt:
            elapsed = self.timer_controller.stop_speech_timer()
            self._handle_timer_stop(speech_type, config, elapsed)
    
    def _handle_timer_stop(self, speech_type: SpeechType, config: Dict, elapsed: int):
        """Handle timer stop and record speech"""
        if elapsed > 0:
            print(f"\n\nTimer stopped at {elapsed // 60:02d}:{elapsed % 60:02d}")
            speaker_name = input("Enter speaker name: ").strip()
            
            if speaker_name:
                record = self.record_manager.add_record(speech_type, speaker_name, elapsed)
                DisplayManager.show_speech_recorded(
                    speaker_name, 
                    config['name'], 
                    record.duration_formatted
                )
            else:
                print("No speaker name provided. Speech not recorded.")
        
        input("\nPress Enter to continue...")
    
    def _handle_view_records(self):
        """Handle viewing speech records"""
        self.record_manager.display_records()
        input("\nPress Enter to continue...")
    
    def _handle_exit(self):
        """Handle application exit"""
        DisplayManager.show_goodbye_message()
        return False
    
    def _handle_invalid_choice(self):
        """Handle invalid menu choice"""
        DisplayManager.show_invalid_choice()
        time.sleep(1)
    
    def _handle_keyboard_interrupt(self):
        """Handle Ctrl+C interrupt"""
        if self.timer_controller.is_timer_running():
            self.timer_controller.stop_speech_timer()
        print("\n\nExiting application...")
    
    def get_app_statistics(self) -> Dict:
        """Get application statistics"""
        return {
            "total_records": self.record_manager.get_records_count(),
            "timer_running": self.timer_controller.is_timer_running(),
            "available_speech_types": len(SpeechConfig.get_all_configs())
        }


def main():
    """Main entry point"""
    app = ToastmasterTimerApp()
    app.run()


if __name__ == "__main__":
    main()
