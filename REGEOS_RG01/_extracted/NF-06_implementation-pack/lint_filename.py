import os
import re
import datetime

ALLOWED_FUNCS = {"TXT","AUD","VID","COD","SYN","IMG","VRL"}
ALLOWED_SCOPES = {"MOD","PRJ","SYS","RIT","TMP"}
ALLOWED_LANGS = {"EN","UNV","JA"}
ALLOWED_TAGS = {"ASSET","SCRIPT","SOURCE","EXPORT","DOC","PATCH","MANIFEST","MODULE","SEED","TEMPLATE","NODE","RITUAL"}
ALLOWED_SLUGS = {
 "introRewrite","citationFix","structureShift","summaryEdit","footnoteAdd","grammarCorrect","rewriteThesis","addExamples","refineArgument","metadataUpdate",
 "bassBoost","reverbCut","eqLowEnd","timingAlign","compressionAdd","vocalBalance","stereoSpread","fadeIn","fadeOut","noiseGateAdd",
 "colorBalance","fadeOverlay","subtitleSync","cutTransition","speedRamp","resolutionScale","aspectFix","noiseReduce","captionAdd","brightnessAdjust",
 "refactorLoop","authPatch","varRename","apiConnector","optimizeQuery","addTests","bugFix","improveLogging","updateDependencies","docCommentAdd",
 "seedShift","patternTune","outputLimit","tokenAdjust","styleBias","paramSweep","modelFineTune","generatePreview","remixLayer","chainExtend",
 "contrastAdjust","gammaCorrect","resizeCrop","vectorizeAsset","filterApply","layerMerge","exportPNG","compressJPG","maskCreate","watermarkAdd",
 "scaleAdjust","collisionFix","lightingTune","shaderUpdate","rigBind","textureSwap","spawnPointSet","environmentMap","frameRateFix","markerPlace"
}

FILENAME_PATTERN = re.compile(
 r'^(?P<func>[A-Z]+)-(?P<scope>[A-Z]+)-(?P<format>[A-Z]+)_(?P<lang>[A-Z]+)-(?P<id>\d{6})-'
 r'(?P<version>V\d+\.\d+\.\d+)\.(?P<ritual>R\d+)_(?P<slugs>[A-Za-z0-9+]+)_'
 r'(?P<date>\d{4}-\d{2}-\d{2})\.(?P<tag>[A-Z]+)\.(?P<hash>[0-9A-F]+)$'
)

def validate_filename(fname):
 errs=
 m = FILENAME_PATTERN.match(fname)
 if not m:
 errs.append("Pattern mismatch")
 return errs
 parts = m.groupdict()
 if parts['func'] not in ALLOWED_FUNCS:
 errs.append(f"Invalid FUNC {parts['func']}")
 if parts['scope'] not in ALLOWED_SCOPES:
 errs.append(f"Invalid SCOPE {parts['scope']}")
 if parts['lang'] not in ALLOWED_LANGS:
 errs.append(f"Invalid LANG {parts['lang']}")
 if parts['tag'] not in ALLOWED_TAGS:
 errs.append(f"Invalid TAG {parts['tag']}")
 slugs = parts['slugs'].split('+')
 if len(slugs)>3:
 errs.append("Too many slugs")
 for s in slugs:
 if s not in ALLOWED_SLUGS:
 errs.append(f"Unknown slug {s}")
 try:
 datetime.date.fromisoformat(parts['date'])
 except:
 errs.append(f"Bad date {parts['date']}")
 return errs

def main(dir):
 invalid={}
 for f in os.listdir(dir):
 errs=validate_filename(f)
 if errs:
 invalid[f]=errs
 if invalid:
 for f, errs in invalid.items():
 print(f"{f}: {errs}")
 else:
 print("All valid [OK]")

if __name__=="__main__":
 import sys
 main(sys.argv[1] if len(sys.argv)>1 else ".")
