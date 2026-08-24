# RC10.0 Server-State Preview

This release is the first server-state foundation. It deliberately does NOT yet
move LM Studio/Qwen into a detached background worker. The working staged
research path is preserved while browser-owned state is replaced with a
persistent server assessment record.

## Persistent assessment identity

Each case gets:
- assessment_uuid
- workbook SHA-256 fingerprint
- immutable server copy of the uploaded workbook
- Human-settings UUID/revision
- server state version
- active job UUID/stage

The case identity is tied to workbook fingerprint + project + product + region +
plant + base currency.

## Refresh / browser recovery

The landing screen now supports:
- upload a workbook;
- resume a recent server assessment without uploading the workbook again.

A full browser refresh therefore does not need to recreate the project from
Streamlit session_state. The server workbook copy and SQLite assessment state
can be reattached.

## Cross-browser state

A second browser can load the same persisted assessment. The top workflow has
a "Reload server state" control.

State_version uses optimistic locking. If another browser/user changed the same
assessment, a stale browser cannot silently overwrite the newer server state.

## Human-factor governance

Human assumptions are stored as immutable revisions:
- settings_uuid
- assessment_uuid
- revision number
- content hash
- reviewer
- Draft / Approved state

Identical Human settings are deduplicated rather than generating meaningless
new revisions.

## Canonical workflow state

The top workflow, Overview progress and Market runtime read the same canonical
state. A downstream artifact proves its prerequisite, preventing impossible
displays such as FX complete while BOM is shown incomplete.

Market progress is dynamic; the denominator is the generated research plan and
is not hard-coded to six.

The Market tab no longer shows a large red Run button while work is active.
The manual action is a smaller Start / refresh selected research action and is
hidden when the server job is active.

## Research / AI job UUIDs

Market research, regional evidence backfill and AI synthesis atomically claim a
server job UUID. Claiming a job advances state_version, so an already-open stale
browser is prevented from overwriting a newly started job.

Market topic status is persisted BEFORE each long LM Studio topic request and
again after completion. Another browser can therefore reload server state and
see the real current topic / resolved count.

The existing SQLite per-topic research checkpoint remains in place for retry
after a topic error or timeout.

## Workbook / report lineage

Generated Excel analysis workbooks now include an Assessment Metadata sheet
containing assessment_uuid, Human-settings UUID and workbook fingerprint.
The Project Risk Summary and PDF report also carry these identifiers.

## Not yet included

A true detached server worker / AI queue is the next architecture step. In this
preview the long LM Studio call is still executed by the Streamlit process that
started it, although its job identity and progress are persisted server-side.

Role-based Viewer / Editor / Reviewer / Admin authorization and the simplified
Main vs Backend UI are also intentionally deferred until the server execution
model is proven.
