from langchain.prompts import PromptTemplate

def get_prompt_template(schema: str):
    return PromptTemplate(
        input_variables=["question"],
        template=f"""
Tu es un assistant expert SQL.
Voici le schéma simplifié de la base de données :
{schema}
Ta tâche :
- Lis le message ci-dessous et génère une requête SQL SQLite.
- Ne réponds que par la requête.
Q: {{question}}
"""
    )
