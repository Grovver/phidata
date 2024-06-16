import json
from phi.llm.openai import OpenAIChat
from phi.assistant.duckdb import DuckDbAssistant

# Define the semantic model as a dictionary
semantic_model = {
    "tables": [
        {
            "name": "maazanh",
            "description": "maazanh Table provide Monthly report for all EzorLahatz. each month ezorlahatz is reporting the leakages (=Phat_Clali) in the EzorLahatz.",
            "path": "maazanh.csv",  # Local path to the Excel file
        }
    ]
}

# Convert the semantic model to a JSON string
semantic_model_json = json.dumps(semantic_model)

# Create an OpenAIChat object
llm = OpenAIChat(model="gpt-4o")

# Create a DuckDbAssistant object for data analysis
data_analyst = DuckDbAssistant(llm=llm, semantic_model=semantic_model_json)

# Execute the first query and print the response
data_analyst.print_response(
    # "What is the Phat_Clali for each EzorLahatz, build a table with the Year, Month,EzorLahatz, Phat_Clali, SUM_AhuzPhatClali columns. where Merhav=0003 and EzorLahatz not NULL. LIMIT=20",
     ##"List 10  EzorLahatz most leakage in 2022, build a table with the Year, Month,EzorLahatz, Phat_Clali, SUM_AhuzPhatClali , calcultae the monthly avarge of AhuzPhatClali columns. where Merhav=0003 and EzorLahatz not NULL. LIMIT=1000",
    # "List 10  EzorLahatz most leakage in October  2022, build a table with the Year, Month,EzorLahatz, Phat_Clali, SUM_AhuzPhatClali columns. where Merhav=0003 and EzorLahatz not NULL. LIMIT=20",
    #"Create a pivot table: Rows Ezor_Lahatz, Columns Year,Month Value Phat_Clali. where Merhav=0003 and Ezor_Lahatz not NULL. LIMIT=1000. save to file EzoreiLahatz_Leakage",
  # "הצג רשימה של אזורי לחץ",
#   "מה הסכום של צריכה לפי תת מפעל בשנת 2024 ובחודש ינואר",
"הצג את אחוז הפחת  לפי חודשים לשנת 2024 בנוסף לכל חודש הצג טמפרטורה ממוצעת בישראל",
#"מה איזור הלחץ שבו הייתה הצריכה הכי גבוהה בחודש ינואר 2024",
#"הצג את אחוז הפחת  לפי מרחב וחודשים לשנת 2024",
#"הצג את כל אזורי הלחץ אליהם יש מכירה באזור לחץ 4-056",
    markdown=False,
    show_sql=False,
    show_result=True,
    show_visual=False
)

"""
# Execute the second query and print the response
data_analyst.print_response(
    "What is the sum Phat_Clali where nodename = mekorot",
    markdown=True,
    show_sql=True,
    show_result=True,
    show_visual=True
)
"""
"""
# Execute the third query and print the response
data_analyst.print_response(
    "Show me a histogram of ratings. Choose a SUM_Phat_Clali size",
    markdown=True
)
"""