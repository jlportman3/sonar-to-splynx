# Normalized Migration Schema Plan

## Step 1: Inventory Source Collections
- [x] Enumerate all Sonar collections captured in the Postgres backup (`graphql_backup__*`).
- [x] Capture sample field structures for key domains (accounts, services, billing, inventory, network, security, support) to understand nested relationships.
- [x] Identify missing or sparse collections that may need special handling.

## Step 2: Draft Normalized Intermediate Schema
- [x] Group the domains above into canonical normalized entities.
- [x] Define core attributes for each normalized entity aligned with Splynx requirements.
- [x] Note required relationships (e.g., accounts ↔ services ↔ invoices).

## Step 3: Map Sonar → Normalized Fields
- [ ] Document field-level mappings for each normalized entity, including transformations, enum harmonization, and ID strategies.
- [ ] Capture relationship mappings (parent/child, many-to-many) and any necessary junction tables.
- [ ] Highlight fields needing derived values or lookups.

## Step 4: Plan Splynx Load Path
- [ ] Decide per-entity whether insertion goes through Splynx REST, direct DB writes, or hybrid.
- [ ] Align normalized schema fields with Splynx schema expectations and validation rules.
- [ ] Document ordering/dependency of load steps (e.g., create tariffs before assigning services).

## Step 5: Prototype ETL Components
- [ ] Build scripts to read Postgres samples and populate normalized tables or in-memory models.
- [ ] Validate transformations with sample data and refine mappings.
- [ ] Outline loaders to push normalized data into Splynx (stubs or actual code).
