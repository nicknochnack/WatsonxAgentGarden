
# A. Agentic RAG
Steps to add agentic rag 
1. Select add knowledge source
2. Choose other sources, upload your chosen pdf 
3. Add the knowledge source description below 
4. Prompt with some of the sample prompts below ➡️ your agent will call the knowledge base tool

>This knowledge covers AIA Fund Rules. These Rules set out:
>1. the requirements for all Members;
>2. the rules regarding payment of Benefits by AIA Health Insurance Pty Ltd;
>3. the ways in which AIA Health Insurance Pty Ltd will conduct the Fund and make decisions regarding all Members; and
>4. all Members are bound by these Rules as amended from time to time.

<a href="https://www.aia.com.au/en/help-and-support/forms-docs#tabfilter-05e20a84e2-item-5412a97eff-tab">RAG Source</a>

Prompts: 
- Summarise the fund rules for AIA
- explain it to me like I'm 5
- can i suspend my membership?

# B. Guidelines 
Steps to add Guidelines (think of these as cached instructions/prompts) 
1. Select Add Guidelines 
2. Populate with the details below 
### Name 
>Direct Debit
### Condition
>If the customer requests information around direct debit details then do not provide an answer advise the customer to fill in the docusign form below.
### Action
>In order to change your Direct Debit details, all you have to do is fill out the Secure Docusign form below: https://powerforms.docusign.net/068e49e0-9e97-4783-b75d-793c9c5fd350?env=au&acct=f5702cdf-a901-446f-bbb8-31046047d20d&accountId=f5702cdf-a901-446f-bbb8-31046047d20d
3. Prompt with `can you give me direct debit details`

# C. Quoting 
1. Import the python tool using `uv run orchestrate tools import -f quoting.py -r requirements.txt -k python`
2. Add the tool to the agent by selecting Add tool > Add from local instance > life_insurance_quote
3. Test out a prompt

Prompts
- give me a life insurance quote ➡️ you should be prompted for your age, smoking and drinking habits and whether you've had heart problems now or in the past.


# D. Policy Submission with Langflow x FastAPI

1. Start fastapi server: `uv run fastapi run 1.Insurance/api.py --port 8018`
2. Add custom component into Langflow Desktop flow 
3. Add mcp server to watsonx orchestrate `uvx mcp proxy http://host.docker.internal:7860/api/v1/mcp/project/<youruuidhere>/sse` 
4. Add the Insurance flow 
5. Test a prompt 

Prompts
- Submit the policy quote from above
- Submit this quote Name: Nick Renotte, DOB: 01012001, Quote Price: $300
