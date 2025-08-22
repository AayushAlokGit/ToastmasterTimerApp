# Toastmaster Timer App - v2.0

A modular Python console application designed to help Toastmaster members and clubs time speeches with visual color indicators.

## Features

- **Visual Timing System**: Changes terminal background color to signal remaining time

  - 🟢 **Green**: Good time remaining
  - 🟡 **Yellow**: Caution - approaching time limit
  - 🔴 **Red**: Time limit reached

- **Grace Period Management**:

  - 🟠 **Grace Period Started**: Clear notification when grace period begins
  - ⚠️ **Grace Period Over**: Alert when speaker is disqualified
  - Real-time countdown during grace period

- **Multiple Speech Types**: Pre-configured timing for different speech categories

  - **Ice Breaker Speech**: 4-6 minutes (Green at 4min, Yellow at 5min, Red at 6min)
  - **Usual Speech**: 5-7 minutes (Green at 5min, Yellow at 6min, Red at 7min)
  - **Speech Evaluation**: 2-3 minutes (Green at 2min, Yellow at 2:30min, Red at 3min)
  - **Table Topic Speech**: 1-2 minutes (Green at 1min, Yellow at 1:30min, Red at 2min)
  - **Test Speech**: Quick testing (Green at 30s, Yellow at 1min, Red at 1:30min)

- **Speech Recording**: Automatically saves speaker names, speech types, and timing data
- **Records Management**: View historical speech records with timestamps

## Project Structure

The application is now organized into modular components:

```
ToastmasterTimerApp/
├── main.py                 # Main application entry point (recommended)
├── toastmaster_timer.py    # Legacy entry point (backward compatibility)
├── speech_types.py         # Speech type definitions and configurations
├── timer_engine.py         # Core timer functionality
├── display_manager.py      # All display and UI functionality
├── record_manager.py       # Speech record management
├── __init__.py            # Package initialization
├── requirements.txt        # Dependencies (none for core app)
├── speech_records.json    # Auto-generated speech records
└── README.md              # This file
```

## Installation & Usage

### Prerequisites

- Python 3.6 or higher
- Windows PowerShell (for color terminal support)

### Running the Application

1. Clone or download this repository
2. Open PowerShell/Command Prompt in the project directory
3. **Recommended**: Run the new modular version:
   ```bash
   python main.py
   ```
4. **Alternative**: Run the legacy version for backward compatibility:
   ```bash
   python toastmaster_timer.py
   ```

### How to Use

1. **Select Speech Type**: Choose from the main menu (1-5)
2. **Start Timer**: Confirm your selection to begin timing
3. **Monitor Progress**: Watch the terminal background change colors as time progresses
4. **Grace Period Alerts**: See clear notifications when grace period starts and ends
5. **Stop Timer**: Press `Ctrl+C` when the speaker finishes
6. **Record Speech**: Enter the speaker's name to save the record

## Timer Signals & Grace Periods

The application follows official Toastmaster timing guidelines:

| Speech Type  | Duration | Green Signal | Yellow Signal | Red Signal | Grace Period |
| ------------ | -------- | ------------ | ------------- | ---------- | ------------ |
| Ice Breaker  | 4-6 min  | 4:00         | 5:00          | 6:00       | 30s          |
| Usual Speech | 5-7 min  | 5:00         | 6:00          | 7:00       | 30s          |
| Evaluation   | 2-3 min  | 2:00         | 2:30          | 3:00       | 30s          |
| Table Topic  | 1-2 min  | 1:00         | 1:30          | 2:00       | None         |
| Test Speech  | Test     | 0:30         | 1:00          | 1:30       | 15s          |

### Grace Period Features

- **Start Notification**: Clear 2-second alert when grace period begins
- **Active Status**: Real-time countdown showing remaining grace time
- **End Notification**: 2-second alert when speaker is disqualified
- **Visual Indicators**: Different emojis for each grace period stage

## Module Documentation

### `speech_types.py`

- Defines `SpeechType` enum and `TimerColor` enum
- Contains `SpeechConfig` class with all timing configurations
- Utility methods for getting grace periods and timing information

### `timer_engine.py`

- `TimerEngine`: Core timer functionality with threading
- `TimerController`: High-level timer management
- Handles grace period notifications and color transitions

### `display_manager.py`

- `DisplayManager`: All terminal display functionality
- Terminal color management (Windows PowerShell compatible)
- Menu displays, notifications, and timer information

### `record_manager.py`

- `SpeechRecord`: Individual speech record representation
- `RecordManager`: Save, load, and display speech records
- JSON-based persistent storage

### `main.py`

- `ToastmasterTimerApp`: Main application coordinator
- Handles user interaction and component integration
- Clean separation of concerns

## Technical Details

- **Architecture**: Modular design with clear separation of concerns
- **Threading**: Background timer with main thread UI handling
- **Error Handling**: Graceful handling of interruptions and file operations
- **Compatibility**: Backward compatible with original single-file version
- **Storage**: JSON-based persistent record storage
- **Platform**: Optimized for Windows PowerShell color support

## Contributing

This is a personal project for Toastmaster clubs. The new modular structure makes contributions easier:

- Each module has a specific responsibility
- Clean interfaces between components
- Comprehensive error handling
- Easy to test individual components

## License

Open source - feel free to use and modify for your Toastmaster club's needs.
