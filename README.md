# MonteCarlo

SCA Monte Carlo + AI Cost Risk Platform.

Current published build: **10.0-RC10.0-ServerState-Preview**.

## Current repository status

The GitHub project has been initialized with the RC10 server-state release notes, version metadata, runtime/dependency files, MCP helper, mock gateway, and launch scaffolding.

The complete RC10 application build is maintained as the packaged release artifact while the remaining large source modules are being transferred into the repository. No workbook, API key, local database, cached market evidence, or user/project data is committed.

## RC10 direction

- persistent assessment UUID
- workbook SHA-256 fingerprint
- Human-setting UUID/revisions
- canonical workflow state
- cross-browser/server-state reload
- optimistic locking for concurrent users
- dynamic market research task counts
- governed Monte Carlo outputs

See `RC10_SERVER_STATE_PREVIEW.md` for the detailed architecture and current boundary before the detached server worker/queue phase.
