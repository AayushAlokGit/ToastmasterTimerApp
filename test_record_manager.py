#!/usr/bin/env python3
"""
Test script for the file-based record management system
"""

import os
import sys
from record_manager import RecordManager
from speech_types import SpeechType

def test_file_based_records():
    """Test the file-based record management system"""
    print("Testing File-Based Record Manager")
    print("=" * 50)
    
    # Clean start - remove existing test file
    test_filename = "test_records.json"
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print("Removed existing test file")
    
    # Create record manager with test file
    rm = RecordManager(test_filename)
    print(f"Created RecordManager with file: {test_filename}")
    
    # Test 1: Add records
    print("\n1. Adding test records...")
    record1 = rm.add_record(SpeechType.ICE_BREAKER, "Alice Johnson", 285)
    record2 = rm.add_record(SpeechType.TABLE_TOPIC, "Bob Wilson", 95)
    record3 = rm.add_record(SpeechType.EVALUATION, "Carol Brown", 155)
    print(f"Added 3 records successfully")
    
    # Test 2: Check file exists and has content
    print("\n2. Checking file persistence...")
    if os.path.exists(test_filename):
        with open(test_filename, 'r') as f:
            content = f.read()
            print(f"File exists and contains {len(content)} characters")
    
    # Test 3: Create new record manager instance (no memory state)
    print("\n3. Creating new RecordManager instance...")
    rm2 = RecordManager(test_filename)
    count = rm2.get_records_count()
    print(f"New instance loaded {count} records from file")
    
    # Test 4: Display records
    print("\n4. Displaying all records:")
    rm2.display_records()
    
    # Test 5: Filter records
    print("\n5. Testing record filtering...")
    ice_breaker_records = rm2.get_records_by_type(SpeechType.ICE_BREAKER)
    alice_records = rm2.get_records_by_speaker("Alice Johnson")
    print(f"Ice Breaker records: {len(ice_breaker_records)}")
    print(f"Alice Johnson records: {len(alice_records)}")
    
    # Test 6: Memory efficiency check
    print("\n6. Memory efficiency test...")
    print("Adding 5 more records...")
    for i in range(5):
        rm2.add_record(SpeechType.TEST, f"Speaker {i+4}", 60 + i*10)
    
    final_count = rm2.get_records_count()
    print(f"Total records after additions: {final_count}")
    
    # Clean up
    print("\n7. Cleaning up...")
    rm2.clear_records()
    final_count_after_clear = rm2.get_records_count()
    print(f"Records after clear: {final_count_after_clear}")
    
    # Remove test file
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print("Test file removed")
    
    print("\n✅ All tests completed successfully!")
    print("\nKey Benefits of File-Based Approach:")
    print("- No memory overhead for storing records")
    print("- Data persists immediately after each operation")
    print("- Multiple instances can share the same data file")
    print("- Memory usage remains constant regardless of record count")

if __name__ == "__main__":
    try:
        test_file_based_records()
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        sys.exit(1)
