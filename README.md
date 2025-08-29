# Toastmaster Timer App - v2.1

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
  - **Prepared Speech**: 5-7 minutes (Green at 5min, Yellow at 6min, Red at 7min)
  - **Speech Evaluation**: 2-3 minutes (Green at 2min, Yellow at 2:30min, Red at 3min)
  - **Table Topic Speech**: 1-2 minutes (Green at 1min, Yellow at 1:30min, Red at 2min)
  - **Test Speech**: Quick testing (Green at 5s, Yellow at 10s, Red at 15s)

- **Speech Recording**: Automatically saves speaker names, speech types, and timing data
- **Records Management**: View historical speech records with timestamps
- **Dynamic Menu Generation**: Menu automatically updates based on configured speech types

## Project Structure

The application is organized into a clean modular architecture:

```
ToastmasterTimerApp/
├── main.py                    # Main application entry point
├── src/                       # Core application modules
│   ├── __init__.py           # Package initialization
│   ├── speech_types.py       # Speech type definitions and configurations
│   ├── timer_engine.py       # Core timer functionality with threading
│   ├── display_manager.py    # Terminal display and color management
│   └── record_manager.py     # File-based speech record management
├── requirements.txt          # Dependencies (none for core app)
├── speech_records.json      # Auto-generated speech records
├── ARCHITECTURE.md          # Technical architecture documentation
├── FILE_BASED_RECORDS.md    # Record management documentation
└── README.md               # This file
```

## Installation & Usage

### Prerequisites

- Python 3.7 or higher
- Windows PowerShell (for color terminal support)

### Running the Application

1. Clone or download this repository
2. Navigate to the project directory
3. **Create virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```
4. **Activate virtual environment**:
   ```bash
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   ```
5. **Run the application**:
   ```bash
   python main.py
   ```

### How to Use

1. **Select Speech Type**: Choose from the dynamically generated main menu (1-5)
2. **Enter Speaker Name**: Provide the speaker's name for record keeping
3. **Start Timer**: Press Enter to begin timing
4. **Monitor Progress**: Watch the terminal background change colors as time progresses
5. **Grace Period Alerts**: See clear notifications when grace period starts and ends
6. **Stop Timer**: Press `Ctrl+C` when the speaker finishes
7. **View Records**: Use menu option 6 to view historical speech records

## Timer Signals & Grace Periods

The application follows official Toastmaster timing guidelines:

| Speech Type     | Duration | Green Signal | Yellow Signal | Red Signal | Grace Period |
| --------------- | -------- | ------------ | ------------- | ---------- | ------------ |
| Ice Breaker     | 4-6 min  | 4:00         | 5:00          | 6:00       | 30s          |
| Prepared Speech | 5-7 min  | 5:00         | 6:00          | 7:00       | 30s          |
| Evaluation      | 2-3 min  | 2:00         | 2:30          | 3:00       | 30s          |
| Table Topic     | 1-2 min  | 1:00         | 1:30          | 2:00       | None         |
| Test Speech     | Test     | 0:05         | 0:10          | 0:15       | 10s          |

### Grace Period Features

- **Start Notification**: Clear 2-second alert when grace period begins
- **Active Status**: Real-time countdown showing remaining grace time
- **End Notification**: 2-second alert when speaker is disqualified
- **Visual Indicators**: Different emojis for each grace period stage

## Module Documentation

### `src/speech_types.py`

- Defines `SpeechType` enum and `TimerColor` enum
- Contains `SpeechConfig` class with all timing configurations
- Utility methods for getting grace periods and timing information

### `src/timer_engine.py`

- `TimerEngine`: Core timer functionality with threading
- `TimerController`: High-level timer management
- Handles grace period notifications and color transitions

### `src/display_manager.py`

- `DisplayManager`: All terminal display functionality
- Terminal color management (Windows PowerShell compatible using cmd color commands)
- Dynamic menu generation from speech type configurations
- Menu displays, notifications, and timer information

### `src/record_manager.py`

- `SpeechRecord`: Individual speech record representation
- `RecordManager`: Save, load, and display speech records
- JSON-based persistent file storage

### `main.py`

- `ToastmasterTimerApp`: Main application coordinator
- Handles user interaction and component integration
- Clean separation of concerns with proper module imports

## Technical Details

- **Architecture**: Clean modular design with src/ directory structure
- **Threading**: Background timer with main thread UI handling
- **Color Management**: Fixed color persistence issues using cmd color commands
- **Error Handling**: Graceful handling of interruptions and file operations
- **Dynamic Menus**: Menu generation automatically reflects configuration changes
- **Storage**: JSON-based persistent record storage with file-based operations
- **Platform**: Optimized for Windows PowerShell with cmd fallback for color support
- **Virtual Environment**: Recommended setup for isolated Python environment

## Recent Updates (v2.1)

- **Fixed Color Persistence**: Resolved terminal color remaining red after timer sessions
- **Dynamic Menu Generation**: Menu automatically updates based on speech type configurations
- **Enhanced Error Handling**: Improved handling of keyboard interrupts and color resets
- **Module Organization**: Moved core modules to src/ directory for better structure
- **Updated Test Timing**: Test speech now uses 5-second intervals for faster testing

## Contributing

This is a personal project for Toastmaster clubs. The new modular structure makes contributions easier:

- Each module has a specific responsibility
- Clean interfaces between components
- Comprehensive error handling
- Easy to test individual components

## License

Open source - feel free to use and modify for your Toastmaster club's needs.
