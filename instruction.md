You have an Apache-style access log at `/app/access.log`. Each non-empty line records one HTTP request in Combined Log Format. Parse the log and write a JSON report to `/app/report.json`.

The report must be a single JSON object with exactly three keys:

- `total_requests` (integer): the total number of non-empty lines in the log.
- `unique_ips` (integer): the number of distinct client IP addresses (the first whitespace-delimited field on each line).
- `top_path` (string): the request path that appears most frequently. The path is the second token inside the quoted request field (e.g., for `"GET /index.html HTTP/1.1"` the path is `/index.html`).

Success criteria:

1. `/app/report.json` exists and contains valid JSON with all three keys listed above.
2. `total_requests` equals the number of non-empty lines in the log.
3. `unique_ips` equals the number of distinct client IP addresses.
4. `top_path` is the request path with the highest count.

You have 120 seconds to complete this task.