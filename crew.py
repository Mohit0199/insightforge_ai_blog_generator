from crewai import Crew, Process
from tasks import research_task, write_task, seo_task, edit_task, social_task
from agents import researcher, writer, seo_optimizer, editor, social_media_promoter


class BlogCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        # Configure the crew
        crew = Crew(
            agents=[
                researcher,
                writer,
                seo_optimizer,
                editor,
                social_media_promoter
            ],
            tasks=[
                research_task,
                write_task,
                seo_task,
                edit_task,
                social_task
            ],
            process=Process.sequential,
            memory=False,
            full_output=True,
            verbose=True,
            share_crew=True,
        )

        # Execute the crew
        inputs = {'topic': self.topic}
        result = crew.kickoff(inputs=inputs)

        return result