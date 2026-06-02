def get_board_info(board: str, subject: str):
    """
    Returns the specific pattern, sections, and marks distribution for a given board and subject.
    This acts as the knowledge base for exam structures.
    """
    patterns = {
        "CBSE": {
            "Science": {
                "total_marks": 80,
                "time_allowed": "3 Hours",
                "style_guidelines": "Questions must strictly align with Class 10 NCERT competency standards. Include Assertion-Reasoning (AR) questions. Include Case-Based Questions (CBQs) that require analytical thinking.",
                "few_shot_examples": [
                    "Q. Assertion (A): Following is a balanced chemical equation: 3Fe + 4H2O -> Fe3O4 + 4H2. Reason (R): The law of conservation of mass holds good for a chemical equation.",
                    "Q. Read the following case: A student adds water to a white powder. It produces a hissing sound and heat. (a) Identify the powder. (b) Write the balanced reaction."
                ],
                "general_instructions": [
                    "This question paper consists of 39 questions in 5 sections.",
                    "All questions are compulsory. However, an internal choice is provided in some questions.",
                    "Section A consists of 20 objective type questions carrying 1 mark each.",
                    "Section B consists of 6 Very Short questions carrying 02 marks each.",
                    "Section C consists of 7 Short Answer type questions carrying 03 marks each.",
                    "Section D consists of 3 Long Answer type questions carrying 05 marks each.",
                    "Section E consists of 3 source-based/case-based units of assessment of 04 marks each."
                ],
                "sections": [
                    {"name": "Section A", "type": "Objective", "num_questions": 20, "marks_per_question": 1},
                    {"name": "Section B", "type": "Very Short Answer", "num_questions": 6, "marks_per_question": 2},
                    {"name": "Section C", "type": "Short Answer", "num_questions": 7, "marks_per_question": 3},
                    {"name": "Section D", "type": "Long Answer", "num_questions": 3, "marks_per_question": 5},
                    {"name": "Section E", "type": "Case Based", "num_questions": 3, "marks_per_question": 4}
                ]
            }
            # Additional subjects can be added here
        },
        "ICSE": {
            "Science": {
                 "total_marks": 80,
                 "time_allowed": "2 Hours",
                 "style_guidelines": "Questions must align with CISCE Class 10 standards. Focus heavily on precise definitions, numericals requiring mandatory SI units, balanced chemical equations, and labeled anatomical/physiological diagrams.",
                 "few_shot_examples": [
                     "Q. (a) Define guttation. (b) Write a balanced chemical equation for the reaction between dilute sulphuric acid and zinc.",
                     "Q. A convex mirror is used as a rearview mirror. Explain giving two reasons based on its optical properties."
                 ],
                 "general_instructions": [
                     "Answers to this Paper must be written on the paper provided separately.",
                     "You will not be allowed to write during the first 15 minutes.",
                     "Section A is compulsory. Attempt any four questions from Section B."
                 ],
                 "sections": [
                     {"name": "Section A (Compulsory)", "type": "Short Answer & MCQs", "num_questions": 40, "marks_per_question": 1},
                     {"name": "Section B (Attempt 4 out of 6)", "type": "Long Answer with Subparts", "num_questions": 4, "marks_per_question": 10}
                 ]
            }
        },
        "WB": {
            "Science": {
                "total_marks": 90,
                "time_allowed": "3 Hours 15 Minutes",
                "style_guidelines": "Questions must align with West Bengal Board (WBBSE) Class 10 standards (Madhyamik). Use straightforward definitions, standard textbook-style derivations, and direct theoretical/numerical questions.",
                "few_shot_examples": [
                    "Q. State Boyle's law. Mathematically express it.",
                    "Q. What is the relation between the focal length and radius of curvature of a spherical mirror?"
                ],
                "general_instructions": [
                    "Regular candidates must answer all questions.",
                    "First 15 minutes are for reading the question paper."
                ],
                "sections": [
                    {"name": "Group A", "type": "Multiple Choice Questions", "num_questions": 15, "marks_per_question": 1},
                    {"name": "Group B", "type": "Very Short Answer", "num_questions": 21, "marks_per_question": 1},
                    {"name": "Group C", "type": "Short Answer", "num_questions": 9, "marks_per_question": 2},
                    {"name": "Group D", "type": "Long Answer", "num_questions": 12, "marks_per_question": 3}
                ]
            }
        }
    }
    
    # Fallback to CBSE Science if not found for testing purposes
    board_data = patterns.get(board, patterns["CBSE"])
    return board_data.get(subject, board_data.get("Science"))
