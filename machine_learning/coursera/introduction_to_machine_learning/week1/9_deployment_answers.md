## deployments
- shadow mode 
  - ML system shadows the human and runs in parallel. 
  - ML system’s output not used for any decisions during this phase. 
  - Sample outputs and verify predictions of ML system
- canary
  - Roll out to small fraction (say 5%) of traffic initially.
  - Monitor system and ramp up traffic gradually
## On a new social media platform, you’re rolling out a new anti-spam system to flag and hide spammy posts. Your team decides to roll out the anti-spam filter via a canary deployment, and roll it out to 1% of users initially. Which of these would you advocate?
- Monitor that 1% of users’ reaction, and either gradually ramp up (if it’s going well) or rollback (if not) 

## for the easy cases (such as an obvious case of the common cold) the system will give a recommendation directly, and for the harder cases it will pass the case on to a team of in-house doctors who will form their own diagnosis independently. What degree of automation are you implementing in this example for patient care? 
- Partial Automation

## anti-spam system . Which of these will result in either concept drift or data drift?
- 
Spammers trying to change the wording used in emails to get around your spam filter.

- deployment is an `iterative process` - make multiple adjustments (such as metrics monitored using dashboards or percentage of traffic served) to work towards optimizing the system.