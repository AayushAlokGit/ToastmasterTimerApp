"""
Speech type definitions and configurations for the Toastmaster Timer App
"""

from enum import Enum
from typing import Dict, List, Tuple


class SpeechType(Enum):
    """Enumeration of different speech types in Toastmaster meetings"""
    ICE_BREAKER = "ice_breaker"
    PREPARED = "prepared"
    EVALUATION = "evaluation"
    TABLE_TOPIC = "table_topic"
    TEST = "test"


class TimerColor(Enum):
    """Timer color states for visual feedback"""
    BLANK = ""
    GREEN = "green"
    YELLOW = "yellow" 
    RED = "red"


class SpeechConfig:
    """Speech configuration data and utilities"""
    
    SPEECH_CONFIGS = {
        SpeechType.ICE_BREAKER: {
            "name": "Ice Breaker Speech",
            "duration_range": "4-6 minutes",
            "timings": [(240, TimerColor.GREEN), (300, TimerColor.YELLOW), (360, TimerColor.RED)],
            "grace_period": 30
        },
        SpeechType.PREPARED: {
            "name": "Prepared Speech",
            "duration_range": "5-7 minutes",
            "timings": [(300, TimerColor.GREEN), (360, TimerColor.YELLOW), (420, TimerColor.RED)],
            "grace_period": 30
        },
        SpeechType.EVALUATION: {
            "name": "Speech Evaluation",
            "duration_range": "2-3 minutes", 
            "timings": [(120, TimerColor.GREEN), (150, TimerColor.YELLOW), (180, TimerColor.RED)],
            "grace_period": 30
        },
        SpeechType.TABLE_TOPIC: {
            "name": "Table Topic Speech",
            "duration_range": "1-2 minutes",
            "timings": [(60, TimerColor.GREEN), (90, TimerColor.YELLOW), (120, TimerColor.RED)],
            "grace_period": 0
        },
        SpeechType.TEST: {
            "name": "Test Speech",
            "duration_range": "Color changes every 5s",
            "timings": [(5, TimerColor.GREEN), (10, TimerColor.YELLOW), (15, TimerColor.RED)],
            "grace_period": 10
        }
    }
    
    @classmethod
    def get_config(cls, speech_type: SpeechType) -> Dict:
        """Get configuration for a specific speech type"""
        return cls.SPEECH_CONFIGS.get(speech_type, {})
    
    @classmethod
    def get_all_configs(cls) -> Dict[SpeechType, Dict]:
        """Get all speech configurations"""
        return cls.SPEECH_CONFIGS
    
    @classmethod
    def get_red_time(cls, speech_type: SpeechType) -> int:
        """Get the time when red signal starts for a speech type"""
        config = cls.get_config(speech_type)
        if config and config.get('timings'):
            return config['timings'][-1][0]  # Last timing is red
        return 0
    
    @classmethod
    def get_grace_end_time(cls, speech_type: SpeechType) -> int:
        """Get the time when grace period ends for a speech type"""
        config = cls.get_config(speech_type)
        if config and config.get('grace_period', 0) > 0:
            red_time = cls.get_red_time(speech_type)
            return red_time + config['grace_period']
        return 0
