<%*
function now() {
  let d = new Date();
  return d.toISOString().slice(0,10);
}
let fn = '';
fn += await tp.system.prompt("FUNC (TXT,AUD,VID,COD,SYN,IMG,VRL)", "TXT") + "-";
fn += await tp.system.prompt("SCOPE (MOD,PRJ,SYS,RIT,TMP)", "PRJ") + "-";
fn += await tp.system.prompt("FORMAT (MD,MP4,MP3,PY)", "MD") + "_";
fn += await tp.system.prompt("LANG (EN,UNV,JA)", "EN") + "-";
fn += await tp.system.prompt("ID (e.g., 000001)", "000001") + "-";
fn += await tp.system.prompt("VERSION (V1.0.0)", "V1.0.0") + ".";
fn += await tp.system.prompt("RITUAL (R0)", "R0") + "_";
fn += await tp.system.prompt("SLUGS (a+b)", "init") + "_";
fn += now() + ".";
fn += await tp.system.prompt("TAG (ASSET,SCRIPT...)", "DOC") + ".";
fn += await tp.system.prompt("HASH", "000000");
tR += fn;
%>

# New MythOS Note  
Filename: `<% tp.file.cursor(0) %>`  
