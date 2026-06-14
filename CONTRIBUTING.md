# Contributing to fuseiq-templates

Thank you for your interest in contributing! We welcome community
contributions to make fuseiq-templates better.

## How to Contribute

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Add or improve a template example under `examples/`.
4. Make sure your example has its own `README.md` and is self-contained
   (no hardcoded API keys, no real credentials).
5. Run the example to verify it works end-to-end.
6. Submit a Pull Request.

## Guidelines

- Each example must have a clear one-line description in its `README.md`.
- Do not commit real tokens, secrets, or `.env` files.
- Use mock data or free/public APIs whenever possible.
- If a real API key is required, document it clearly in the example's
  `README.md` and use an environment variable.
- Format Python code with `ruff` or `black` before submitting.
- Keep examples concise — under 200 lines unless absolutely necessary.

## Code of Conduct

Be respectful and constructive. We're all here to learn and build cool
things with FuseIQ.

## Questions?

Open an issue or join our community at https://fuseiq.io
