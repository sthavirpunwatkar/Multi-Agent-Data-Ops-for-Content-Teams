import argparse
from scripts.agents.outliner import OutlinerAgent
from scripts.utils import load_text, load_json

def main(prd_path, sources_path, out_path):
    prd_text = load_text(prd_path)
    sources = load_json(sources_path)

    agent = OutlinerAgent()
    outline = agent.run(prd_text, sources, out_path)
    print(f"Outline saved to: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prd", default="data/prd_example.md", help="PRD file path")
    parser.add_argument("--sources", default="data/sources.json", help="Sources JSON path")
    parser.add_argument("--out", default="data/outline.json", help="Output path")
    args = parser.parse_args()
    main(args.prd, args.sources, args.out)
