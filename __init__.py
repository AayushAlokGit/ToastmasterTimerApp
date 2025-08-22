"""
Toastmaster Timer App Package
A modular Python application for timing Toastmaster speeches with visual feedback.
"""

from .speech_types import SpeechType, TimerColor, SpeechConfig
from .timer_engine import TimerEngine, TimerController
from .record_manager import RecordManager, SpeechRecord
from .display_manager import DisplayManager
from .main import ToastmasterTimerApp

__version__ = "2.0.0"
__author__ = "Toastmaster Timer App"

__all__ = [
    'SpeechType', 
    'TimerColor', 
    'SpeechConfig',
    'TimerEngine', 
    'TimerController',
    'RecordManager', 
    'SpeechRecord',
    'DisplayManager',
    'ToastmasterTimerApp'
]
