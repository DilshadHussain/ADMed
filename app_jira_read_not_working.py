from atlassian import Jira

# Replace with your Jira instance URL and credentials
jira = Jira(
    url='http://ber-jirapp-001v.hub.calyxhosting.com:8080/',
    username='hussaid',
    password='Year2024.09'
)

# JQL query to fetch issues
jql = 'project = CMT AND status IN ("In UAT") ORDER BY issuekey'
issues = jira.jql(jql)

# Print the retrieved issues
print(issues)
