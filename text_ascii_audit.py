import argparse,csv,json,sys
def transform(value):
    return [{"index":i,"char":c,"codepoint":f"U+{ord(c):04X}"} for i,c in enumerate(value) if ord(c)>127]

def main():
    parser=argparse.ArgumentParser(description='Text ASCII auditor')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    data=source
    result=transform(data)
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
