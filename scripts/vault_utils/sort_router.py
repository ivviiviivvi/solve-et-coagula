import os
import shutil

def sort_file(filename):
    f = filename.lower()
    if "feedback" in f: return "PD-GG_00-00_guidance-protocols/feedback/"
    if "draft" in f or "proto" in f: return "NR-TH_00-00_narrative-threads/fragments/"
    if "gpt" in f or "chat" in f: return "XP-PR_00-00_experiments-live/"
    return "FL-TR_00-00_anomaly-stream/"

if __name__ == "__main__":
    test_files = ["gpt_ideas.md", "lesson_feedback.md", "proto_song.txt", "loose_note.md"]
    for f in test_files:
        path = sort_file(f)
        print(f"{f} → {path}")
