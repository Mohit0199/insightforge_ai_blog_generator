from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatLiteLLM

# Load environment variables
load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Instantiate the LiteLLM wrapper for Gemini
llm = ChatLiteLLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Basic tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Custom tools using BaseTool
class SEOAnalysisTool(BaseTool):
    name: str = "SEO Analysis Tool"
    description: str = "Analyzes text for SEO optimization opportunities"
    
    def _run(self, text: str) -> str:
        prompt = f"""
        Analyze this text for SEO optimization:
        {text}
        Provide recommendations on:
        1. Primary keyword opportunities
        2. Secondary keywords to include
        3. Heading structure improvements
        4. Meta description suggestion
        5. Readability improvements
        """
        result = llm([HumanMessage(content=prompt)])
        return result.content

class GrammarCheckTool(BaseTool):
    name: str = "Grammar Check Tool"
    description: str = "Checks and corrects grammar in text"
    
    def _run(self, text: str) -> str:
        prompt = f"""
        Please check and correct the grammar in this text:
        {text}
        Return the corrected version with explanations of major changes.
        """
        result = llm([HumanMessage(content=prompt)])
        return result.content

class SocialMediaTool(BaseTool):
    name: str = "Social Media Post Generator"
    description: str = "Generates platform-specific social media posts"
    
    def _run(self, text: str, platform: str) -> str:
        prompt = f"""
        Create a {platform} post based on this content:
        {text}
        Include:
        - Appropriate length for the platform
        - Relevant hashtags
        - Engaging emojis
        - A call-to-action
        """
        result = llm([HumanMessage(content=prompt)])
        return result.content

# Instantiate custom tools
seo_tool = SEOAnalysisTool()
grammar_tool = GrammarCheckTool()
social_tool = SocialMediaTool()

# Group tools
research_tools = [search_tool, scrape_tool]
writing_tools = []
seo_tools = [seo_tool]
editing_tools = [grammar_tool]
social_media_tools = [social_tool]