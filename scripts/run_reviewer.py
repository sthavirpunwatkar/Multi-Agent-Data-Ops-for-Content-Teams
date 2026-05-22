import argparse
from scripts.agents.reviewer import ReviewerAgent
from scripts.utils import load_text

def main(draft_path, prd_path, out_path):
    draft_content = load_text(draft_path)
    prd_text = load_text(prd_path)

    agent = ReviewerAgent()
    reviewed_draft = agent.run(draft_content, prd_text, out_path)
    print(f"Reviewed draft saved to: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--draft", default="data/draft.md", help="Draft Markdown path")
    parser.add_argument("--prd", default="data/prd_example.md", help="PRD file path")
    parser.add_argument("--out", default="data/reviewed_draft.md", help="Output path")
    args = parser.parse_args()
    main(args.draft, args.prd, args.out)
