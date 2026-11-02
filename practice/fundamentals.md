# Fundamentals worth revisiting

Answer without notes, then consult a primary reference and correct your explanation. A useful answer has a mechanism, an example and a limit. Revisit at days 20, 40, 60, 80 and 100.

## Linux and networking

1. What happens between entering a hostname and receiving an HTTPS response?
2. How do you distinguish a DNS failure, TCP refusal, TLS error and HTTP 503?
3. What does a process share with other processes in a container environment?
4. Why does listening on 0.0.0.0 differ from listening on 127.0.0.1?
5. Which permissions are needed to read a file versus traverse its parent directory?
6. How would you investigate a full disk without deleting unknown files?

## Cloud and identity

7. What is the difference between an identity, a role and a permission?
8. Which trust relationship allows a pipeline to obtain short-lived credentials?
9. How can a VM have outbound access without accepting unsolicited inbound traffic?
10. Why can a zero-traffic application still generate cloud charges?
11. Which resources might remain after deleting the main compute service?

## Delivery and infrastructure

12. What makes a build reproducible? What is outside your current controls?
13. Why should deployment use an immutable artifact identity?
14. What should happen when a pull request comes from an untrusted fork?
15. How does infrastructure state differ from configuration?
16. What is drift, and when might automatic reconciliation be harmful?
17. What can make rolling back application code unsafe after a data migration?

## Data and distributed systems

18. When does a cache return stale data, and why might that be acceptable?
19. How can a queue deliver the same job twice? How would the consumer handle that?
20. What failure does replication address, and what failures still require backups?
21. How do you choose between synchronous and asynchronous communication?
22. What does consensus provide beyond maintaining multiple data copies?
23. What is the tradeoff between increasing timeouts and retrying sooner?

## Reliability and observability

24. Why can every process be alive while users cannot complete their task?
25. How do readiness and liveness probes produce different actions?
26. What question does each of a log, metric and trace help answer?
27. Why is user ID often a poor label for a high-volume metric?
28. How does a request-based error budget differ from a time-based one?
29. What evidence shows that a backup is recoverable?
30. What makes a postmortem action measurable and verifiable?

## Show your reasoning

Choose one question. Give an initial answer, draw a mechanism, run a small experiment and cite the reference you used. Preserve your original answer so you can see how your understanding changed.
