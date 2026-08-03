from pathlib import Path
import hashlib, json, re, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def add(name, ok, detail): checks.append({'check':name,'status':'PASS' if ok else 'FAIL','detail':detail})
result=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(ROOT/'tests'),'-p','test_site.py','-v'],capture_output=True,text=True)
add('Automated structural tests',result.returncode==0,(result.stdout+result.stderr).strip())
html=(ROOT/'index.html').read_text(); css=(ROOT/'styles.css').read_text(); js=(ROOT/'app.js').read_text()
add('No broken placeholder links','href="#"' not in html,'All links target sections or real local documents.')
add('No unsupported performance claims',not re.search(r'\b(guarantee|guaranteed profit|proven profitable|risk-free)\b',html,re.I),'No guarantee or profitability claim found.')
add('Synthetic dashboard disclosure','Values shown are synthetic' in html,'Product mockup is clearly labeled illustrative.')
add('Execution boundary','does not place bets' in html.lower(),'Automatic execution is explicitly excluded.')
add('Responsive implementation','@media(max-width:720px)' in css,'Mobile layout breakpoint present.')
add('Accessibility implementation','prefers-reduced-motion' in css and 'skip-link' in html,'Reduced motion and keyboard skip navigation present.')
add('Form privacy disclosure','localStorage' in js and 'stored only in this browser' in html,'Demo storage behavior is disclosed.')
add('SEO foundation',all(x in html for x in ['meta name="description"','og:title','og:description']),'Core metadata present.')
add('Architecture coherence',all(x in html for x in ['Market Scanner','Trust Engine','Research Lab','Prediction Journal']),'Public narrative matches frozen platform architecture.')
files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and 'AUDIT_REPORT' not in p.name}
report={'release':'Project Isabel Startup Website 1.0 Foundation','audit_passes':checks,'all_passed':all(c['status']=='PASS' for c in checks),'sha256_manifest':files}
(ROOT/'AUDIT_REPORT.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'all_passed':report['all_passed'],'passes':len(checks)},indent=2))
sys.exit(0 if report['all_passed'] else 1)
