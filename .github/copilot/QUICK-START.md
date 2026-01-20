# Quick Reference: Copilot Workflow Commands

## For New Lecture (CREATE mode):

Open Copilot Chat and type:
```
Execute .github/copilot/workflow-create.md for ThermoS26-01
```

That's it! Replace `ThermoS26-01` with your filename.

---

## For Updated Lecture (UPDATE mode):

```
Execute .github/copilot/workflow-update.md for ThermoS26-01
```

---

## Process Multiple Files at Once:

```
Execute .github/copilot/workflow-create.md for ThermoS26-01, ThermoS26-02, ThermoS26-03
```

---

## Troubleshooting

If Copilot asks for confirmation:
```
Execute .github/copilot/workflow-create.md for ThermoS26-01 autonomously without stopping for confirmation
```

If it doesn't start:
1. Try selecting "Agent" mode in the chat picker
2. Or add "DO IT NOW" to your command

---

## What Happens

The workflow file contains all the detailed instructions, so you just reference it with a short command. Copilot reads the workflow file and executes all 4 steps automatically.

**One line command = Complete transcription!**
