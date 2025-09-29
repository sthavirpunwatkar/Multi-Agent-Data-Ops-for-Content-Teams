import argparse
from scripts.agents.researcher import ResearcherAgent
from scripts.utils import load_text

def main(prd_path, out_path):
    prd_text = load_text(prd_path)
    agent = ResearcherAgent()
    sources = agent.run(prd_text, out_path)
    print("Sources saved:", sources)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prd", required=True, help="PRD file path")
    parser.add_argument("--out", default="data/sources.json", help="Output path")
    args = parser.parse_args()
    main(args.prd, args.out)
