"""
Speech record management for the Toastmaster Timer App
"""

import json
import os
from datetime import datetime
from typing import List, Dict
from speech_types import SpeechType


class SpeechRecord:
    """Represents a single speech record"""
    
    def __init__(self, speech_type: SpeechType, speaker_name: str, duration_seconds: int):
        self.timestamp = datetime.now().isoformat()
        self.speech_type = speech_type.value
        self.speaker_name = speaker_name
        self.duration_seconds = duration_seconds
        self.duration_formatted = f"{duration_seconds // 60:02d}:{duration_seconds % 60:02d}"
    
    def to_dict(self) -> Dict:
        """Convert record to dictionary for JSON serialization"""
        return {
            "timestamp": self.timestamp,
            "speech_type": self.speech_type,
            "speaker_name": self.speaker_name,
            "duration_seconds": self.duration_seconds,
            "duration_formatted": self.duration_formatted
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SpeechRecord':
        """Create SpeechRecord from dictionary"""
        record = cls.__new__(cls)
        record.timestamp = data.get("timestamp", "")
        record.speech_type = data.get("speech_type", "")
        record.speaker_name = data.get("speaker_name", "")
        record.duration_seconds = data.get("duration_seconds", 0)
        record.duration_formatted = data.get("duration_formatted", "00:00")
        return record


class RecordManager:
    """Manages speech records - saving, loading, and displaying with file-based operations"""
    
    def __init__(self, filename: str = "speech_records.json"):
        self.filename = filename
        # Ensure the file exists with empty array if it doesn't exist
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Ensure the records file exists with proper structure"""
        if not os.path.exists(self.filename):
            try:
                with open(self.filename, 'w') as f:
                    json.dump([], f, indent=2)
            except Exception as e:
                print(f"Warning: Could not create records file - {e}")
    
    def add_record(self, speech_type: SpeechType, speaker_name: str, duration_seconds: int):
        """Add a new speech record directly to file"""
        record = SpeechRecord(speech_type, speaker_name, duration_seconds)
        
        try:
            # Read existing records
            existing_records = self._read_records_from_file()
            
            # Add new record
            existing_records.append(record.to_dict())
            
            # Write back to file
            with open(self.filename, 'w') as f:
                json.dump(existing_records, f, indent=2)
                
            return record
            
        except Exception as e:
            print(f"Warning: Could not save record - {e}")
            return record
    
    def _read_records_from_file(self) -> List[Dict]:
        """Read all records from file and return as list of dictionaries"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            return []
        except Exception as e:
            print(f"Warning: Could not load records - {e}")
            return []
    
    def save_records(self):
        """Legacy method - kept for backward compatibility but no longer needed"""
        # This method is no longer needed since we write directly to file
        # Kept for backward compatibility
        pass
    
    def load_records(self):
        """Legacy method - kept for backward compatibility but no longer needed"""
        # This method is no longer needed since we read directly from file
        # Kept for backward compatibility
        pass
    
    def get_all_records(self) -> List[SpeechRecord]:
        """Get all speech records by reading from file"""
        try:
            data = self._read_records_from_file()
            return [SpeechRecord.from_dict(item) for item in data]
        except Exception as e:
            print(f"Warning: Could not retrieve records - {e}")
            return []
    
    def display_records(self):
        """Display all speech records in a formatted table by reading from file"""
        records = self.get_all_records()
        
        if not records:
            print("\nNo speech records found.")
            return
        
        print(f"\n{'='*80}")
        print("SPEECH RECORDS")
        print(f"{'='*80}")
        print(f"{'Date/Time':<20} {'Speaker':<20} {'Type':<20} {'Duration':<10}")
        print(f"{'-'*80}")
        
        for record in records:
            timestamp = datetime.fromisoformat(record.timestamp).strftime("%Y-%m-%d %H:%M")
            speech_type = record.speech_type.replace('_', ' ').title()
            print(f"{timestamp:<20} {record.speaker_name:<20} {speech_type:<20} {record.duration_formatted:<10}")
    
    def get_records_count(self) -> int:
        """Get total number of records by reading from file"""
        try:
            data = self._read_records_from_file()
            return len(data)
        except Exception:
            return 0
    
    def clear_records(self):
        """Clear all records by writing empty array to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump([], f, indent=2)
        except Exception as e:
            print(f"Warning: Could not clear records - {e}")
    
    def get_records_by_type(self, speech_type: SpeechType) -> List[SpeechRecord]:
        """Get records filtered by speech type"""
        try:
            all_records = self.get_all_records()
            return [record for record in all_records if record.speech_type == speech_type.value]
        except Exception as e:
            print(f"Warning: Could not filter records - {e}")
            return []
    
    def get_records_by_speaker(self, speaker_name: str) -> List[SpeechRecord]:
        """Get records filtered by speaker name"""
        try:
            all_records = self.get_all_records()
            return [record for record in all_records if record.speaker_name.lower() == speaker_name.lower()]
        except Exception as e:
            print(f"Warning: Could not filter records - {e}")
            return []
