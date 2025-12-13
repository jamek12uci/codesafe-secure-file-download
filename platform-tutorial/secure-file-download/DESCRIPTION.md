\# Secure File Download Service



\## Scenario



You are a junior software engineer working on an internal developer tools team.

Your team maintains a small Python-based service that allows authenticated users

to download documentation files from a shared directory on the server.



A recent security audit revealed that the service may be vulnerable to a

directory traversal attack, potentially allowing attackers to access files

outside the intended directory.



Your task is to investigate the existing code, understand how the vulnerability

works, and implement a fix that prevents malicious file paths from being used —

without breaking existing functionality.



\## Objective



Modify the provided Python source code so that:

\- Valid files inside the allowed directory can still be downloaded

\- Attempts to access files outside the directory are blocked

\- Existing functionality continues to work correctly



Run the provided test cases to verify your solution.  

When all tests pass, a flag will be printed.



