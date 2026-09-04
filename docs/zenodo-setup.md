# Zenodo DOI Setup

Zenodo can mint a **DOI** for this repository after it is linked to GitHub.
This cannot be fully completed from the CLI without your Zenodo login.

## Steps (about 5 minutes)

1. Make sure the GitHub repo is **Public**  
   https://github.com/jasonlhw-rgb/FinReport-NLP

2. Sign in to Zenodo with GitHub (or link GitHub in account settings):  
   https://zenodo.org/account/settings/github/

3. Find **FinReport-NLP** in the repository list and flip **ON**.

4. Prefer creating / syncing a GitHub Release (e.g. `v0.1.0`).  
   Zenodo will create a deposit and assign a DOI such as `10.5281/zenodo.xxxxxxx`.

5. Open the Zenodo record → copy the DOI → send it back (or update locally):
   - `CITATION.cff` → add `doi: "10.5281/zenodo.xxxxxxx"`
   - `README.md` Citation section → add the badge/link

Repository metadata for Zenodo is prepared in [`.zenodo.json`](../.zenodo.json).

## After you have the DOI

Reply with the DOI string, and it can be written into `CITATION.cff` / README automatically.
