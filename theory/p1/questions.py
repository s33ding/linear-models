import sys
import os

# Add parent directory so `shared_func` becomes visible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../aws')))

from shared_func.bedrock_func import run_bedrock

def analyze_understanding(user_response, topic):
    """Analyze user understanding using Bedrock"""
    prompt = f"""Analyze this student's understanding of {topic}:
Student response: "{user_response}"

Rate their understanding (1-5) and provide brief feedback on what they got right and what needs improvement. Keep it concise."""
    
    try:
        return run_bedrock(prompt)
    except Exception as e:
        return f"Error analyzing: {e}"

def ask_question(topic, understanding_question, mc_question, options, correct_answer):
    """Ask understanding question, then multiple choice"""
    print(f"\n=== {topic} ===")
    print(f"First, {understanding_question}")
    user_understanding = input("Your answer: ")
    
    print("\nAnalyzing your understanding...")
    analysis = analyze_understanding(user_understanding, topic)
    print(f"Analysis: {analysis}")
    
    print(f"\nNow the multiple choice question:")
    print(mc_question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Your choice (number): "))
            if 1 <= choice <= len(options):
                if choice == correct_answer:
                    print("✅ Correct!")
                else:
                    print(f"❌ Wrong. Correct answer: {correct_answer}")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def main():
    questions = [
        {
            "topic": "Covariance",
            "understanding": "what do you understand about covariance and how it measures relationships between variables?",
            "mc_question": "What does a positive covariance indicate?",
            "options": [
                "Variables move in opposite directions",
                "Variables move in the same direction", 
                "Variables are independent",
                "One variable is constant"
            ],
            "correct": 2
        },
        {
            "topic": "Pearson Correlation",
            "understanding": "explain what Pearson correlation measures and its range of values?",
            "mc_question": "What is the range of Pearson correlation coefficient?",
            "options": [
                "0 to 1",
                "-∞ to +∞",
                "-1 to 1",
                "0 to 100"
            ],
            "correct": 3
        },
        {
            "topic": "Matrix Determinant",
            "understanding": "what does the determinant of a matrix tell us about the matrix?",
            "mc_question": "When is a matrix NOT invertible?",
            "options": [
                "When determinant = 1",
                "When determinant = 0",
                "When determinant > 0",
                "When determinant < 0"
            ],
            "correct": 2
        },
        {
            "topic": "PCA",
            "understanding": "what is PCA and what problem does it solve?",
            "mc_question": "PCA finds which of the following?",
            "options": [
                "Minimum variance directions",
                "Eigenvectors of correlation matrix",
                "Eigenvectors of covariance matrix",
                "Random projections"
            ],
            "correct": 3
        },
        {
            "topic": "Spearman Correlation",
            "understanding": "how does Spearman correlation differ from Pearson correlation?",
            "mc_question": "Spearman correlation is based on:",
            "options": [
                "Raw data values",
                "Ranked data values",
                "Squared differences",
                "Absolute differences"
            ],
            "correct": 2
        }
    ]
    
    print("Linear Models Quiz - Understanding Assessment")
    print("=" * 50)
    
    for q in questions:
        ask_question(q["topic"], q["understanding"], q["mc_question"], q["options"], q["correct"])
    
    print("\n🎉 Quiz completed!")

if __name__ == "__main__":
    main()
