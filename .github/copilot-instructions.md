<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Toastmaster Timer App

This is a Python console application for timing Toastmaster speeches with visual color indicators.

## Project Status - v2.1 (COMPLETED)

- [x] Verify that the copilot-instructions.md file in the .github directory is created.
- [x] Clarify Project Requirements - Python console app for Toastmaster speech timing
- [x] Scaffold the Project - Created main application with src/ directory structure
- [x] Customize the Project - Implemented full timer functionality with color changes and speech recording
- [x] Install Required Extensions - No extensions needed (uses standard library only)
- [x] Compile the Project - Python application runs successfully in virtual environment
- [x] Create and Run Task - Application tested and working
- [x] Launch the Project - Successfully launched and tested
- [x] Ensure Documentation is Complete - README.md, ARCHITECTURE.md, and copilot-instructions.md updated
- [x] Fixed Color Persistence - Resolved terminal color remaining after timer sessions
- [x] Dynamic Menu Generation - Menu automatically reflects speech type configurations
- [x] Module Organization - Moved core modules to src/ directory structure

## Current Architecture

```
ToastmasterTimerApp/
├── main.py                    # Application entry point and coordinator
├── src/                       # Core application modules
│   ├── speech_types.py       # Domain model (enums and configurations)
│   ├── timer_engine.py       # Business logic (timer and threading)
│   ├── display_manager.py    # Presentation layer (UI and color management)
│   └── record_manager.py     # Data layer (file-based persistence)
├── requirements.txt          # Dependencies
├── speech_records.json      # Runtime-generated data file
└── documentation/            # Architecture and API docs
```

## Speech Types and Timing

- Ice Breaker Speech: 4-6 minutes (Green at 4min, Yellow at 5min, Red at 6min)
- Prepared Speech: 5-7 minutes (Green at 5min, Yellow at 6min, Red at 7min)
- Speech Evaluation: 2-3 minutes (Green at 2min, Yellow at 2:30min, Red at 3min)
- Table Topic Speech: 1-2 minutes (Green at 1min, Yellow at 1:30min, Red at 2min)
- Test Speech: Testing mode (Green at 5s, Yellow at 10s, Red at 15s)

## Key Technical Features

- **Threading Architecture**: Background timer thread with main UI thread
- **Color Management**: Fixed PowerShell compatibility using cmd color commands
- **Dynamic Configuration**: Menu generation automatically reflects speech type changes
- **File-based Storage**: JSON persistence for speech records
- **Grace Period System**: Real-time notifications and countdown
- **Error Handling**: Comprehensive exception handling and color reset strategies

## Development Environment

- Python 3.7+ with virtual environment (recommended)
- Windows PowerShell with cmd fallback for color support
- No external dependencies required (uses standard library only)
