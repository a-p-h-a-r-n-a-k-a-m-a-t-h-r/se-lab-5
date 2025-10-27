1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues were formatting and unused imports, since they only required adding/removing lines or switching to f-strings. Writing docstrings was repetitive but simple.
The hardest issues were the mutable default argument and bare except clauses, because they required deeper understanding of Python behavior and proper exception handling.
Removing eval() also required choosing a safer alternative and thinking about security implications.

2. Did the static analysis tools report any false positives? If so, describe one example.

Most issues reported were valid. However, warnings like using a global variable (W0603) or function naming style (C0103) depend on context. While generally discouraged, they may be reasonable in small scripts or when matching external naming conventions.
So these were not false positives, but more like suggestions with context-dependent justification.

3. How would you integrate static analysis tools into your actual software development workflow?

I would use pre-commit hooks and IDE integration so issues are caught immediately during development.
In CI, I’d run Pylint, Flake8, and Bandit automatically on every pull request, failing the pipeline if severity thresholds are not met.
Also, I’d commit shared configuration files and establish team conventions to keep style consistent.

4. What improvements did you observe in code quality, readability, or robustness?

The code became more secure (removing eval), and safer due to proper exception handling and fixing mutable defaults.
Documentation, formatting, and naming were clearer, making the code easier to read.
Using f-strings, context-managed file operations, and input checks improved maintainability and reduced potential runtime errors.
