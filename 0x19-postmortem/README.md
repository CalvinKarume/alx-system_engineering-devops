This is the 0x19. Postmortem project


Post-Incident Analysis: Web Service Outage
Incident Summary:
- Impact: 
  - Affected primary web service, rendering it inaccessible to around 60% of users.
Chronology:
Detection: 
  - September 12th , 2023, 21:00 EAT
    - Monitoring systems alerted us to a sudden surge in errors and a drop in response times on our web service.
- Response Steps:
  - On-call web engineer, Calvin John, was alerted instantly.
  - Investigation focused on server infrastructure, load balancers, and application code.
  - Initially, we suspected a traffic surge due to a marketing campaign.
- Misleading Investigations:
  - DDoS attack suspicions and database issues were fruitless paths explored initially.
- Escalation:
  - The incident was escalated to the DevOps and Networking teams for additional support.
- Resolution:
  -  September 13th , 2023, 7:45 EAT
  - The root cause was a misconfigured firewall rule that mistakenly blocked incoming traffic from specific IP ranges.
  - We fixed this by correcting the rule and performing a rolling restart of web servers.

Root Cause and Solution:
- Root Cause:
  - The outage resulted from a misconfigured firewall rule, likely introduced during routine maintenance, blocking certain IP addresses.
- Resolution:
  - Corrected the firewall rule to allow the blocked traffic and conducted a rolling server restart.

Corrective and Preventative Measures:
- Enhancements:
  - Automate firewall rule testing, establish stricter peer review, and enhance monitoring for rule changes.
- Action Items:
  1. Implement automated firewall rule testing in development.
  2. Add automated regression tests for critical configurations.
  3. Improve documentation and procedures for firewall rule changes.
  4. Conduct a post-incident review involving all teams for shared insights and improved coordination.
Conclusion:
This incident, which resulted from a misconfigured firewall rule, highlights the necessity of a thorough change management procedure and close supervision in order to guarantee the reliable operation of web services.

