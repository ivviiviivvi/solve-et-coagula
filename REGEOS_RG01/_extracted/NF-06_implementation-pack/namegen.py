import datetime

def generate_filename(func, scope, fmt, lang, id_num, version, ritual, slugs, date, tag, hash_val):
    """
    Constructs a MythOS filename:
    FUNC-SCOPE-FORMAT_LANG-ID-VERSION.RITUAL_slug1+slug2+slug3_YYYY-MM-DD.TAG.HASH
    """
    slugs_part = '+'.join(slugs)
    return f"{func}-{scope}-{fmt}_{lang}-{id_num}-{version}.{ritual}_{slugs_part}_{date}.{tag}.{hash_val}"

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate MythOS filename")
    parser.add_argument("--func", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--fmt", required=True)
    parser.add_argument("--lang", required=True)
    parser.add_argument("--id", dest="id_num", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--ritual", required=True)
    parser.add_argument("--slugs", required=True, help="Comma-separated slugs")
    parser.add_argument("--date", default=datetime.date.today().isoformat())
    parser.add_argument("--tag", required=True)
    parser.add_argument("--hash", dest="hash_val", required=True)
    args = parser.parse_args()
    slugs_list = args.slugs.split(',')
    print(generate_filename(
        args.func.upper(), args.scope.upper(), args.fmt.upper(),
        args.lang.upper(), args.id_num, args.version.upper(),
        args.ritual.upper(), slugs_list, args.date,
        args.tag.upper(), args.hash_val.upper()
    ))
