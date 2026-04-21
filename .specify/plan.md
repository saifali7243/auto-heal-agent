## Architecture

The system runs as a continuous Python agent.

### Components

1. Monitor Module
   - Collects system metrics using psutil

2. Rule Engine
   - Evaluates system state against thresholds

3. Action Engine
   - Executes predefined recovery actions

4. Logger
   - Logs events and actions

5. Main Loop
   - Runs every 5 seconds

## Flow

1. Collect metrics
2. Evaluate rules
3. Trigger actions
4. Log results
5. Repeat
