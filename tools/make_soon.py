#!/usr/bin/env python3
"""Write the 'coming soon' app pages.

The three apps that have not shipped yet all say the same few things in the
same order, so they are generated from one template rather than kept as six
hand-edited files. Run it after editing APPS or the template; the output is
plain static HTML, committed alongside the hand-written pages.

    python3 tools/make_soon.py
"""

from pathlib import Path

WEB = Path(__file__).resolve().parent.parent
MAIL = "hungtt2242@gmail.com"

APPS = {
    "coda": {
        "en": {
            "name": "Coda",
            "title": "Coda — one line a day",
            "desc": "A diary small enough to actually keep: one line a day, on your phone and nowhere else. From Ioniclabs.",
            "h1": ("One line a day. That is the whole ", "diary", "."),
            "sub": "Every evening Coda asks for a single sentence. Not a page, not a prompt, not a streak to protect — one line, and then it leaves you alone.",
            "art": "A year of Coda is 365 lines you will actually read again.",
            "cards": [
                ("What you write", [
                    "One line an evening, and the app closes itself",
                    "Yesterday's line sits above today's, so you write in context",
                    "Search back through every line you have ever written",
                ]),
                ("What it looks like", [
                    "A year on one screen, a dot per day",
                    "The months you kept and the months you missed, honestly drawn",
                    "Read a whole month as a single page",
                ]),
                ("Where it lives", [
                    "One file on your iPhone — no account, no server, no tracking",
                    "Export every line as plain text whenever you like",
                    "Nothing leaves the phone unless you send it yourself",
                ]),
            ],
        },
        "vi": {
            "name": "Coda",
            "title": "Coda — mỗi ngày một dòng",
            "desc": "Một cuốn nhật ký đủ nhỏ để giữ được thật: mỗi ngày một dòng, nằm trên máy bạn và chỉ ở đó. Từ Ioniclabs.",
            "h1": ("Mỗi ngày một dòng. Cuốn ", "nhật ký", " chỉ có thế."),
            "sub": "Mỗi tối Coda hỏi bạn đúng một câu. Không phải một trang, không gợi ý, không chuỗi ngày phải giữ — một dòng, rồi để bạn yên.",
            "art": "Một năm Coda là 365 dòng mà bạn sẽ thật sự đọc lại.",
            "cards": [
                ("Bạn viết gì", [
                    "Mỗi tối một dòng, viết xong app tự đóng",
                    "Dòng hôm qua nằm ngay trên dòng hôm nay, để bạn viết có mạch",
                    "Tìm lại được mọi dòng bạn từng viết",
                ]),
                ("Nhìn ra sao", [
                    "Cả một năm trên một màn hình, mỗi ngày một chấm",
                    "Những tháng bạn giữ được và những tháng bạn bỏ, vẽ đúng như nó là",
                    "Đọc trọn một tháng như đọc một trang",
                ]),
                ("Nằm ở đâu", [
                    "Một tệp trên iPhone của bạn — không tài khoản, không máy chủ, không theo dõi",
                    "Xuất mọi dòng ra chữ thuần lúc nào cũng được",
                    "Không gì rời khỏi máy trừ khi chính bạn gửi đi",
                ]),
            ],
        },
    },
    "ferry": {
        "en": {
            "name": "Ferry",
            "title": "Ferry — the days between here and there",
            "desc": "A countdown for the few dates that actually matter, drawn as a strip of days you can watch get shorter. From Ioniclabs.",
            "h1": ("The few dates that ", "actually matter", "."),
            "sub": "Ferry holds five dates at most, on purpose. Each one is a strip of days, and every morning one more day is crossed off in front of you.",
            "art": "Five dates, five strips, and a home screen widget that keeps counting.",
            "cards": [
                ("Five dates, no more", [
                    "A hard limit, so the list stays the list of what matters",
                    "Each date is a strip of days, not a number you have to feel something about",
                    "Days already spent stay visible — the strip shortens from the front",
                ]),
                ("On your home screen", [
                    "A widget in three sizes, updated at midnight",
                    "Lock screen complications for the nearest date",
                    "A quiet notification on the morning of the day itself",
                ]),
                ("Where it lives", [
                    "One file on your iPhone — no account, no server, no tracking",
                    "Nothing is shared with anyone unless you export it",
                    "Works entirely offline, including the widget",
                ]),
            ],
        },
        "vi": {
            "name": "Ferry",
            "title": "Ferry — những ngày giữa đây và đó",
            "desc": "Đếm ngược cho vài cái hẹn thật sự quan trọng, vẽ thành một dải ngày mà bạn nhìn thấy nó ngắn dần. Từ Ioniclabs.",
            "h1": ("Vài cái hẹn ", "thật sự quan trọng", "."),
            "sub": "Ferry giữ nhiều nhất năm ngày, cố ý như vậy. Mỗi ngày là một dải, và mỗi sáng lại có thêm một ô bị gạch đi trước mắt bạn.",
            "art": "Năm cái hẹn, năm dải ngày, và một widget ngoài màn hình chính vẫn đếm tiếp.",
            "cards": [
                ("Năm cái hẹn, không hơn", [
                    "Một giới hạn cứng, để danh sách vẫn đúng là danh sách những điều quan trọng",
                    "Mỗi cái hẹn là một dải ngày, không phải một con số bắt bạn phải thấy gì đó",
                    "Những ngày đã tiêu vẫn nhìn thấy — dải ngắn dần từ đầu",
                ]),
                ("Ngoài màn hình chính", [
                    "Widget ba cỡ, cập nhật lúc nửa đêm",
                    "Tiện ích màn hình khoá cho cái hẹn gần nhất",
                    "Một thông báo nhẹ vào sáng của chính ngày đó",
                ]),
                ("Nằm ở đâu", [
                    "Một tệp trên iPhone của bạn — không tài khoản, không máy chủ, không theo dõi",
                    "Không chia sẻ với ai trừ khi bạn tự xuất ra",
                    "Chạy hoàn toàn ngoại tuyến, kể cả widget",
                ]),
            ],
        },
    },
    "kiln": {
        "en": {
            "name": "Kiln",
            "title": "Kiln — thirty days to fire one habit",
            "desc": "One habit at a time, thirty days to fire it, and a pot that cracks when you miss a day. From Ioniclabs.",
            "h1": ("Thirty days to fire ", "one habit", "."),
            "sub": "Kiln holds one habit at a time. Each day you keep it, the pot in the kiln gets one layer closer to finished. Miss a day and it cracks — visibly, and then you start it again.",
            "art": "One habit, thirty days, and a pot you can see the state of at a glance.",
            "cards": [
                ("One at a time", [
                    "A single habit, because that is how many you can actually change",
                    "Thirty days, then the pot comes out of the kiln and you pick the next one",
                    "A shelf of everything you have fired before",
                ]),
                ("Honest about misses", [
                    "A missed day cracks the pot instead of quietly resetting a number",
                    "One repair a run, so a bad day does not end the month",
                    "No streak to protect, and no guilt-trip notifications",
                ]),
                ("Where it lives", [
                    "One file on your iPhone — no account, no server, no tracking",
                    "A widget with today's pot and nothing else",
                    "Export your whole shelf whenever you like",
                ]),
            ],
        },
        "vi": {
            "name": "Kiln",
            "title": "Kiln — ba mươi ngày để nung một thói quen",
            "desc": "Mỗi lần một thói quen, ba mươi ngày để nung, và một cái nồi sẽ nứt khi bạn bỏ một ngày. Từ Ioniclabs.",
            "h1": ("Ba mươi ngày để nung ", "một thói quen", "."),
            "sub": "Kiln chỉ giữ một thói quen tại một lúc. Ngày nào bạn giữ được, cái nồi trong lò lại dày thêm một lớp. Bỏ một ngày là nó nứt — nứt thật, nhìn thấy được, rồi bạn nung lại từ đầu.",
            "art": "Một thói quen, ba mươi ngày, và một cái nồi nhìn phát biết đang ra sao.",
            "cards": [
                ("Mỗi lần một cái", [
                    "Đúng một thói quen, vì đó là số bạn thật sự đổi được",
                    "Ba mươi ngày, rồi nồi ra lò và bạn chọn cái tiếp theo",
                    "Một cái kệ đựng tất cả những gì bạn đã nung xong",
                ]),
                ("Thành thật về những ngày bỏ", [
                    "Bỏ một ngày thì nồi nứt, chứ không lặng lẽ đưa một con số về 0",
                    "Mỗi lượt được vá một lần, để một ngày tệ không kết thúc cả tháng",
                    "Không có chuỗi ngày phải giữ, không có thông báo trách móc",
                ]),
                ("Nằm ở đâu", [
                    "Một tệp trên iPhone của bạn — không tài khoản, không máy chủ, không theo dõi",
                    "Một widget chỉ có cái nồi của hôm nay, không gì khác",
                    "Xuất cả cái kệ ra lúc nào cũng được",
                ]),
            ],
        },
    },
}

WORDS = {
    "en": {
        "soon": "Coming soon",
        "eyebrow": "For iPhone · in the workshop",
        "notify": "Tell me when it ships",
        "back": "All apps",
        "note": "Not on the App Store yet. Write to us and you will hear the day it is.",
        "lab": "Ioniclabs",
        "contact": "Contact",
        "other": "Also from the lab",
        "lang": "Tiếng Việt",
        "support": "Support",
        "subject": "Ioniclabs — {name}",
    },
    "vi": {
        "soon": "Sắp có",
        "eyebrow": "Cho iPhone · đang trong xưởng",
        "notify": "Báo tôi khi app ra",
        "back": "Tất cả ứng dụng",
        "note": "Chưa có trên App Store. Viết cho chúng tôi, ngày nó lên bạn sẽ biết đầu tiên.",
        "lab": "Ioniclabs",
        "contact": "Liên hệ",
        "other": "Cũng từ xưởng này",
        "lang": "English",
        "support": "Hỗ trợ",
        "subject": "Ioniclabs — {name}",
    },
}

TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{up}assets/apps/{slug}.svg">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{up}assets/apps/{slug}.svg">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/site.css?v=6">
</head>
<body>

<nav class="ap-nav">
  <img class="icon" src="{up}assets/apps/{slug}.svg" alt="">
  <a class="here" href="./">{name}</a>
  <span class="bar"></span>
  <a href="{lab}">Ioniclabs&nbsp;↗</a>
  <a href="{swap}">{langname}</a>
  <a class="cta" href="mailto:{mail}?subject={subject}">{notify}</a>
</nav>

<main class="ap">

  <section class="ap-hero ap-head">
    <span class="ap-eyebrow">{eyebrow}</span>
    <h1 class="ap-display">{h1a}<em>{h1b}</em>{h1c}</h1>
    <p class="ap-sub">{sub}</p>
    <div class="btn-row">
      <a class="btn" href="mailto:{mail}?subject={subject}">{notify}</a>
      <a class="btn btn--soft" href="{lab}">{back}</a>
    </div>
    <p class="note">{note}</p>
    <div class="ap-stage ap-stage--art">
      <img src="{up}assets/apps/{slug}.svg" alt="">
      <span class="tag tag--soon">{soon}</span>
      <p>{art}</p>
    </div>
  </section>

  <section class="ap-head">
    <h2 class="ap-display">{whath1a}<em>{whath1b}</em>{whath1c}</h2>
    <div class="ap-cards ap-cards--3">
{cards}
    </div>
  </section>

  <footer class="ap-foot">
    <div class="cols">
      <div>
        <div class="sign"><img src="{up}assets/apps/{slug}.svg" alt="">{name}</div>
        <p class="fine" style="margin-top:14px;max-width:30ch">{soon} — {year}</p>
      </div>
      <div>
        <h4>{name}</h4>
        <ul>
          <li><a href="mailto:{mail}?subject={subject}">{notify}</a></li>
          <li><a href="mailto:{mail}?subject={subject}">{support}</a></li>
        </ul>
      </div>
      <div>
        <h4>Ioniclabs</h4>
        <ul>
          <li><a href="{lab}">{back}</a></li>
          <li><a href="mailto:{mail}?subject=Ioniclabs">{contact}</a></li>
        </ul>
      </div>
      <div>
        <h4>{other}</h4>
        <ul>
{siblings}
          <li><a href="{swap}">{langname}</a></li>
        </ul>
      </div>
    </div>
    <p class="fine">{name} © 2026 Ioniclabs</p>
  </footer>

</main>
</body>
</html>
"""

CARD = """      <div class="card">
        <div class="card-head"><span class="dot" style="background:{colour}"></span><h3>{head}</h3></div>
        <ul>
{items}
        </ul>
      </div>"""

COLOURS = {"coda": "#78cfa8", "ferry": "#6aa8f0", "kiln": "#ef8b5a"}

WHAT = {
    "en": ("What ", "{name}", " will do."),
    "vi": ("{name} ", "sẽ làm gì", "."),
}

SIBLING_ORDER = ["tessera168", "coda", "ferry", "kiln"]
SIBLING_NAMES = {"tessera168": "Tessera 168", "coda": "Coda", "ferry": "Ferry", "kiln": "Kiln"}


def build(slug, lang):
    app = APPS[slug][lang]
    w = WORDS[lang]
    up = "../../" if lang == "en" else "../../../"
    lab = "../../" if lang == "en" else "../../"
    swap = ("../../vi/apps/%s/" % slug) if lang == "en" else ("../../../apps/%s/" % slug)
    subject = w["subject"].format(name=app["name"]).replace(" ", "%20").replace("—", "%E2%80%94")

    cards = "\n".join(
        CARD.format(
            colour=COLOURS[slug],
            head=head,
            items="\n".join("          <li>%s</li>" % i for i in items),
        )
        for head, items in app["cards"]
    )

    siblings = "\n".join(
        '          <li><a href="../%s/">%s</a></li>' % (s, SIBLING_NAMES[s])
        for s in SIBLING_ORDER
        if s != slug
    )

    what = [p.format(name=app["name"]) for p in WHAT[lang]]

    html = TEMPLATE.format(
        lang=lang,
        slug=slug,
        up=up,
        lab=lab,
        swap=swap,
        mail=MAIL,
        subject=subject,
        name=app["name"],
        title=app["title"],
        desc=app["desc"],
        h1a=app["h1"][0],
        h1b=app["h1"][1],
        h1c=app["h1"][2],
        sub=app["sub"],
        art=app["art"],
        cards=cards,
        siblings=siblings,
        whath1a=what[0],
        whath1b=what[1],
        whath1c=what[2],
        year="2026",
        langname=w["lang"],
        **{k: w[k] for k in ("soon", "eyebrow", "notify", "back", "note",
                             "contact", "other", "support")},
    )

    out = WEB / ("apps/%s/index.html" % slug if lang == "en" else "vi/apps/%s/index.html" % slug)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    for slug in APPS:
        for lang in ("en", "vi"):
            print(build(slug, lang).relative_to(WEB))
