from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url, academic_search 
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

#model setup 
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)


#1st agent 
def build_search_agent():
    return create_react_agent(
        model = llm,
        tools= [web_search, academic_search],
        prompt="You are an elite research agent. You must invoke the `academic_search` tool to fetch published research papers and PDFs whenever the user's topic involves Science, Technology, Math, Finance, or highly technical concepts. Always use standard `web_search` for general topics."
    )

#2nd agent 

def build_reader_agent():
    return create_react_agent(
        model = llm,
        tools = [scrape_url]
    )


#writer chain 

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Draft an exhaustively detailed and highly comprehensive research report based on the provided data. Do not summarize briefly! Write extensive paragraphs, deeply exploring the exact data so the user requires no external searching. Use formatting heavily to make it readable: use **bold** for key terms, use bullet points, and use `<mark>text</mark>` to highlight crucial insights (Notion-style). Finally, you MUST include a 'Sources' section at the VERY END listing out the reference URLs explicitly as clickable markdown links."),
    ("human", """Research the following topic: {topic}

Use the following gathered data:
{research}

Write the report now:"""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()

#revision_writer_chain

revision_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a master technical writer executing revisions. Revise the provided draft based on the critique. Significantly EXPAND on all details. Do not output brief sentences! Provide a deeply exhaustive, academic-grade rewrite of the document incorporating all data, fixing flaws, and dramatically increasing the depth of analysis. Retain all strict markdown formatting (<mark>, **bold**, 'Sources', etc)."),
    ("human", """Revise the research report below based on the provided feedback.

Topic: {topic}

Original Report:
{draft}

Critic Feedback:
{feedback}

Please provide the final, heavily revised and improved report."""),
])

revision_writer_chain = revision_prompt | llm | StrOutputParser()

#qa_chain

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research assistant. You are answering the user's questions strictly based on the following research report context. If the answer is not in the context, say that the report does not cover it."),
    ("human", """Research Report Context:
{report}

User Question: {question}""")
])

qa_chain = qa_prompt | llm | StrOutputParser()

#tutor_chain

tutor_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Socratic academic tutor. Your goal is NOT to write the essay for the student. Your goal is to synthesize the research into a highly structured academic outline. After the outline, you must pose 3 engaging 'Critical Thinking Questions' to guide the student in writing their own paper. Do not write the final essay body paragraphs."),
    ("human", """Synthesize an outline and 3 critical thinking questions based on this topic and research.

Topic: {topic}

Research context:
{research}""")
])

tutor_chain = tutor_prompt | llm | StrOutputParser()

#fact_checker_chain

fact_checker_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a ruthless Fact Checker. Your job is to read a Final Draft Report and strictly cross-reference it against the Raw Research Context. If ANY factual claim (statistic, name, date, specific event) in the Final Draft is NOT found in the Raw Research Context, you must wrap that specific claim in the output with <span style='color:red; font-weight:bold;'>[UNVERIFIED: claim]</span>. Do NOT change anything else. If a claim is verified, leave it alone. Return the fully checked text."),
    ("human", """Raw Research Context:
{research}

Final Draft Report:
{draft}

Execute the factual cross-reference check now and return the marked-up text:""")
])

fact_checker_chain = fact_checker_prompt | llm | StrOutputParser()
