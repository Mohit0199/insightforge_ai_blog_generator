from crewai import Task
from agents import researcher, writer, seo_optimizer, editor, social_media_promoter
from tools import research_tools, seo_tools, editing_tools, social_media_tools


# Research Task
research_task = Task(
    description=(
    "Conduct in-depth research to identify the next big trend in {topic}. Your analysis should focus on:\n"
    "- Identifying and explaining 3-5 key trends shaping the industry\n"
    "- Analyzing the pros and cons of each trend in detail, including market reception\n"
    "- Assessing the market potential for each trend, considering current and future demand\n"
    "- Evaluating potential risks, including technological, regulatory, or market-based risks\n"
    "Gather information from reputable sources including:\n"
    "- Leading tech news platforms\n"
    "- Peer-reviewed research papers or whitepapers\n"
    "- Comprehensive industry reports and market surveys"
    ),
    expected_output=(
    "Comprehensive research report (3-5 paragraphs) containing:\n"
    "- A detailed summary of each identified trend, including relevant data and expert opinions\n"
    "- An analysis of the pros and cons for each trend, with a clear explanation of their potential impact\n"
    "- A market potential assessment that includes key metrics, target demographics, and growth projections\n"
    "- A risk analysis that outlines technological, regulatory, and market challenges\n"
    "- Clear citations from authoritative sources to back up the findings"
    ),
    tools=research_tools,  # Using the research_tools package from tools.py
    agent=researcher,
    async_execution=False,
    context=None  # This is the first task in the chain
)


# Writing Task
write_task = Task(
    description=(
        "Write a blog post on the topic '{topic}' based on the research report provided.\n\n"
        "The article should follow a clear blog structure, including:\n"
        "- A compelling introduction that hooks the reader\n"
        "- A brief context or background of the topic\n"
        "- 3-5 well-organized sections, each focusing on a specific trend or insight\n"
        "- Use of subheadings (H2 and H3) for readability\n"
        "- Bullet points or numbered lists for key takeaways or data points\n"
        "- Smooth transitions between sections\n"
        "- A strong conclusion with key takeaways and forward-looking insights\n\n"
        "Maintain a clear, engaging, and positive tone. Avoid jargon and ensure that the language is accessible to a general audience."
    ),
    expected_output=(
        "Final draft blog post in Markdown format (.md) that includes:\n"
        "- Word count between 1300 - 1500 words\n"
        "- Proper Markdown headers (## for H2, ### for H3)\n"
        "- Clearly defined blog structure (intro, body with sections, conclusion)\n"
        "- Bullet points or numbered lists for facts or tips\n"
        "- Hyperlinks to sources (if available)\n"
        "- Optimized for readability and flow\n"
        "- Informative yet conversational tone"
    ),
    tools=[],  # Writer relies on LLM capabilities
    agent=writer,
    async_execution=False,
    context=[research_task],  # Depends on research task
    output_file='draft-blog-post.md'
)


# SEO Optimization Task
seo_task = Task(
    description=(
    "Optimize the blog post about {topic} for maximum search engine visibility. Tasks include:\n"
    "- Identifying high-priority primary and secondary keywords based on search volume and relevance\n"
    "- Strategically placing primary and secondary keywords in headings, body text, and meta elements\n"
    "- Improving meta elements (title, description) to increase click-through rates on search results\n"
    "- Enhancing the heading structure to make it SEO-friendly and reader-friendly\n"
    "- Suggesting internal links to relevant content across the site, ensuring a natural flow\n"
    "- Making sure the content meets the readability and user experience standards for SEO"
    ),
    expected_output=(
        "SEO-optimized blog post with the following:\n"
        "- Keyword analysis report with primary and secondary keywords highlighted\n"
        "- Suggested meta title and description with SEO best practices (under 160 characters)\n"
        "- Markdown annotations showing where and how keywords were integrated into headings and body\n"
        "- Recommendations for internal linking opportunities (including anchor text)\n"
        "- Enhanced readability, with suggestions for improving content engagement and reducing bounce rate"
    ),
    tools=seo_tools,
    agent=seo_optimizer,
    async_execution=False,
    context=[write_task],  # Works on writer's output
    output_file='seo-optimized-post.md'
)


# Editing Task
edit_task = Task(
    description=(
        "Polish the blog post about {topic} to ensure it is publication-ready. Focus on:\n"
        "- Correcting grammar, spelling, and punctuation errors throughout the text\n"
        "- Ensuring consistent writing style and tone, with clear and concise language\n"
        "- Enhancing logical flow between sections to ensure smooth transitions\n"
        "- Adding or adjusting content depth to ensure the article is engaging and informative without being too technical\n"
        "- Ensuring proper attribution for sources and correcting any citation issues"
    ),
    expected_output=(
    "Publication-ready blog post with the following:\n"
    "- Tracked changes showing all grammar, style, and content edits made\n"
    "- Editor's notes on major revisions (e.g., content added/removed or restructured)\n"
    "- Final formatted Markdown with appropriate headings, bullet points, and citations\n"
    "- Full approval for publishing, including suggestions for any final tweaks"
    ),
    tools=editing_tools,
    agent=editor,
    async_execution=False,
    context=[seo_task],  # Works on SEO-optimized version
    output_file='final-blog-post.md'
)

# Social Media Task
social_task = Task(
    description=(
        "Create promotional content for the blog post about {topic} including:\n"
        "- 2 Twitter/X posts (280 chars max)\n"
        "- 1 LinkedIn post (professional tone)\n"
        "- 1 Instagram caption (with emojis)\n"
        "- Hashtag suggestions for each platform"
    ),
    expected_output=(
        "Social media package containing:\n"
        "- Platform-specific posts\n"
        "- Hashtag strategies\n"
        "- Suggested posting times\n"
        "- Engagement tips"
    ),
    tools=social_media_tools,
    agent=social_media_promoter,
    async_execution=False,
    context=[edit_task],  # Promotes the final version
    output_file='social-media-kit.md'
)