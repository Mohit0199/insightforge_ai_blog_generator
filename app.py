import streamlit as st
import markdown
from crew import BlogCrew

# --- Page Setup ---
st.set_page_config(page_title="InsightForge Blog Generator", layout="wide")
st.title("Insightforge AI Blog Generator")
st.markdown(
    "Generate a blog post and social media kit in one click using CrewAI agents. "
    "Just enter a topic and let AI do the magic!"
)

# --- Blog Topic Input ---
topic = st.text_input("🎯 Enter a blog topic:", placeholder="e.g. The Rise of Open Source LLMs")

# --- Generate Blog ---
if st.button("Generate Blog & Social Media Kit") and topic.strip():
    with st.spinner("Generating your content... This may take 2-3 minutes ⏳"):
        blog_crew = BlogCrew(topic)
        blog_crew.run()

    st.success("✅ Blog and social media kit generated successfully! Scroll below to preview 👇")

    # --- Final Blog Post ---
    st.markdown("---")
    st.subheader("Final Blog Post")
    try:
        with open("final-blog-post.md", "r", encoding="utf-8") as f:
            final_blog_md = f.read()
        final_blog_html = markdown.markdown(final_blog_md)
        with st.expander("Click to preview the blog post"):
            st.markdown(final_blog_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("❌ 'final-blog-post.md' not found. Please check the generation process.")

    # --- Social Media Kit ---
    st.subheader("Social Media Kit")
    try:
        with open("social-media-kit.md", "r", encoding="utf-8") as f:
            social_kit_md = f.read()
        social_kit_html = markdown.markdown(social_kit_md)
        with st.expander("Click to preview the social media content"):
            st.markdown(social_kit_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("❌ 'social-media-kit.md' not found. Please check the generation process.")
