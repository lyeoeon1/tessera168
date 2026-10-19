#!/usr/bin/env python3
"""Writes Arista's pages: its site, privacy policy and terms of use, in English and Vietnamese.

    apps/arista/                 vi/apps/arista/
    apps/arista/privacy/         vi/apps/arista/privacy/
    apps/arista/terms/           vi/apps/arista/terms/
    arista/                      the short link ioniclabs.app/arista

Arista has its own legal pages (like SupArrive) because it runs a server, sends pictures to AI
services and sells subscriptions with credits. The app links here (`AppInfo` in the Arista
repo), and so does App Store Connect, so these URLs must not move. The in-app privacy policy
(`PrivacyPolicySheet`) tells the same story in shorter words: change both together.

Run from the site's root:  python3 tools/make_arista.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIL = "ioniclabs.support@gmail.com"
CSS = "site.css?v=12"
# Bumped when the screenshots in assets/arista/shots/ change (1.0, no motion: 2026-10-19).
SHOTS_V = 1
EFFECTIVE = {"en": "19 October 2026", "vi": "19/10/2026"}

T = {
    "en": {
        "lang": "en", "other": "vi", "label": "EN",
        "title": "Arista — photos into coloring pages",
        "desc": "Arista turns your photos into coloring pages you color on your iPhone, then keeps your finished art behind a calm focus timer.",
        "eyebrow": "Coloring · Collections · Focus timer",
        "display": "Your photos, <em>ready to color</em>",
        "sub": "Arista turns a photo into a coloring page, gives you brushes, pencils and fills to color it on your iPhone, and keeps the finished art close, on collection boards and behind a calm focus timer.",
        "soon": "Coming soon",
        "soon_p": "Coming to the App Store as Arista Studio. iPhone, in English and Vietnamese.",
        "inside": "What's <em>inside</em>",
        "hero_alt": "Coloring an AI page of a snow globe in Arista.",
        "screens": "Photo in, page out, <em>color</em> it",
        "screens_sub": "Pick a photo and a style, color the page on your iPhone, then keep it on a board or behind the clock.",
        "shots": [("1-home", "Home: a photo and a style", "A photo and a style"),
                  ("2-styles", "The style picker with sample pages", "Dozens of styles"),
                  ("4-focus", "The focus timer with a colored page behind the clock", "Your art behind the clock"),
                  ("5-collections", "Collection templates", "Boards for what you color")],
        "cards": [
            ("📷", "Photo to page", "Take or pick a photo and get a page with clean outlines. The Original style is traced on your iPhone, free and offline; AI styles are drawn by an AI model."),
            ("🖍️", "Color it your way", "Fill, brushes, pencil and pen, palettes and layers of undo. Your artworks and collections stay on your phone."),
            ("🌿", "Collections", "Cut out what you colored and arrange it on boards with stickers and notes."),
            ("⏳", "Focus with it", "A focus timer with your artwork, a soft gradient or your own video behind the clock, floating particles and ambient sounds."),
        ],
        "pricing": "Free to color, credits for the <em>AI</em>",
        "pricing_sub": "Tracing pages on your phone, coloring, collections and the focus timer are free. AI pages use credits: 10 credits for an AI page. Every App Store account gets 30 credits once, to try it.",
        "max_p": "600 credits a month, about 60 AI pages. Every AI style, pencil and pen, all palettes.",
        "ultra_p": "2,000, 4,000 or 8,000 credits a month, for classes, families and creators.",
        "plans_note": "Prices shown are US prices; the App Store shows yours in your currency. Subscriptions renew automatically until cancelled in Settings › Apple Account › Subscriptions. Unused credits roll over while the plan is active, up to three months' worth.",
        "privacy_card": "Your photos stay on your phone unless you use an AI style, and then only after you allow it. No ads, no trackers.",
        "terms_card": "How credits and plans work, what you may make with the AI, and the licence for the app.",
        "more_privacy": "Privacy policy →", "more_terms": "Terms of use →",
        "foot": "Your photos, ready to color.",
        "privacy": "Privacy policy", "terms": "Terms of use", "support": "Support", "home": "Home",
        "all_apps": "All apps", "lang_other": "Tiếng Việt",
        "fine": "Arista is made by Ioniclabs. AI pages are drawn by a third-party AI model and can be imperfect.",
        "contents": "Contents",
    },
    "vi": {
        "lang": "vi", "other": "en", "label": "VI",
        "title": "Arista — biến ảnh thành trang tô màu",
        "desc": "Arista biến ảnh của bạn thành trang tô màu để tô ngay trên iPhone, rồi giữ tranh đã tô làm nền cho đồng hồ tập trung nhẹ nhàng.",
        "eyebrow": "Tô màu · Bộ sưu tập · Đồng hồ tập trung",
        "display": "Ảnh của bạn, <em>sẵn sàng để tô</em>",
        "sub": "Arista biến một bức ảnh thành trang tô màu, cho bạn cọ, bút chì và công cụ đổ màu để tô trên iPhone, và giữ tranh đã tô bên bạn, trên các bảng sưu tập và phía sau đồng hồ tập trung.",
        "soon": "Sắp ra mắt",
        "soon_p": "Sắp có trên App Store với tên Arista Studio. iPhone, tiếng Anh và tiếng Việt.",
        "inside": "Có gì <em>bên trong</em>",
        "hero_alt": "Đang tô một trang AI quả cầu tuyết trong Arista.",
        "screens": "Chọn ảnh, ra trang, <em>tô</em> thôi",
        "screens_sub": "Chọn ảnh và phong cách, tô trang ngay trên iPhone, rồi giữ lại trên bảng sưu tập hoặc phía sau đồng hồ.",
        "shots": [("1-home", "Trang chủ: một bức ảnh và một phong cách", "Ảnh và phong cách"),
                  ("2-styles", "Bảng chọn phong cách với trang mẫu", "Hàng chục phong cách"),
                  ("4-focus", "Đồng hồ tập trung với tranh đã tô phía sau", "Tranh của bạn sau đồng hồ"),
                  ("5-collections", "Mẫu bộ sưu tập", "Bảng cho những gì bạn tô")],
        "cards": [
            ("📷", "Ảnh thành trang", "Chụp hoặc chọn ảnh để có trang với nét viền rõ. Kiểu Original được vẽ ngay trên iPhone, miễn phí và không cần mạng; các kiểu AI do mô hình AI vẽ."),
            ("🖍️", "Tô theo ý bạn", "Đổ màu, cọ, bút chì, bút mực, bảng màu và hoàn tác nhiều bước. Tác phẩm và bộ sưu tập nằm trên điện thoại của bạn."),
            ("🌿", "Bộ sưu tập", "Cắt những gì bạn đã tô và sắp lên các bảng cùng nhãn dán và ghi chú."),
            ("⏳", "Tập trung cùng nó", "Đồng hồ tập trung với tranh của bạn, nền chuyển màu dịu hoặc video của riêng bạn phía sau, hạt bay nhẹ và âm thanh nền."),
        ],
        "pricing": "Tô màu miễn phí, credit cho <em>AI</em>",
        "pricing_sub": "Tạo trang trên điện thoại, tô màu, bộ sưu tập và đồng hồ tập trung đều miễn phí. Trang AI dùng credit: 10 credit cho một trang AI. Mỗi tài khoản App Store được tặng 30 credit một lần để dùng thử.",
        "max_p": "600 credit mỗi tháng, khoảng 60 trang AI. Mọi kiểu AI, bút chì và bút mực, tất cả bảng màu.",
        "ultra_p": "2.000, 4.000 hoặc 8.000 credit mỗi tháng, cho lớp học, gia đình và người sáng tạo.",
        "plans_note": "Giá hiển thị là giá tại Mỹ; App Store hiện giá bằng tiền tệ của bạn. Gói tự gia hạn cho đến khi huỷ trong Cài đặt › Tài khoản Apple › Đăng ký. Credit chưa dùng được cộng dồn khi gói còn hiệu lực, tối đa bằng ba tháng.",
        "privacy_card": "Ảnh của bạn nằm trên điện thoại, trừ khi bạn dùng kiểu AI, và chỉ sau khi bạn cho phép. Không quảng cáo, không theo dõi.",
        "terms_card": "Credit và gói hoạt động thế nào, bạn được tạo gì bằng AI, và giấy phép sử dụng app.",
        "more_privacy": "Chính sách quyền riêng tư →", "more_terms": "Điều khoản sử dụng →",
        "foot": "Ảnh của bạn, sẵn sàng để tô.",
        "privacy": "Chính sách quyền riêng tư", "terms": "Điều khoản sử dụng", "support": "Hỗ trợ", "home": "Trang chủ",
        "all_apps": "Tất cả app", "lang_other": "English",
        "fine": "Arista do Ioniclabs làm. Trang AI do mô hình AI của bên thứ ba vẽ và có thể chưa hoàn hảo.",
        "contents": "Mục lục",
    },
}

# ---------------------------------------------------------------- privacy policy

PRIVACY = {
"en": {
"summary": """<p><strong>In short:</strong> Arista has no ads, no analytics and no trackers, and never asks for your name, email or password. Your photos, pages, collections and palettes stay on your iPhone. A picture leaves your phone only when you make a page in an AI style, and only after you have allowed it: it goes to Arista's server and on to OpenAI, which draws the page, and Arista keeps it at most two days. To count credits, Arista gives your phone an anonymous account, which you can delete in the app under Profile → Delete account.</p>""",
"sections": [
("controller", "1. Who is responsible", f"""<p>Arista (on the App Store as Arista Studio) is made by Ioniclabs, the developer named on its App Store page, which is responsible for the data described here. Privacy contact: <a href="mailto:{MAIL}?subject=Arista">{MAIL}</a>.</p>
<p>This policy covers the Arista iPhone app and this website.</p>"""),
("device", "2. What stays on your phone", """<p>Photos you take or import, the pages you color, your artworks, collections, palettes, focus settings and your profile (the name and color you choose) are stored in the app on your iPhone. They are included in your iCloud or computer backup if you use one, and are deleted when you delete the app. Pages in the Original style are traced entirely on your iPhone; nothing is sent for them.</p>"""),
("account", "3. Your anonymous account", """<p>The first time you open Arista, it creates an anonymous account on its server so that credits and purchases can be counted. You never sign in. The account's key is kept in your iPhone's keychain, so the account survives deleting and reinstalling the app on the same phone.</p>
<div class="sa-table"><table>
<thead><tr><th>Data on Arista's server</th><th>Why</th><th>How long</th></tr></thead>
<tbody>
<tr><td>A random account ID</td><td>To know whose credits are whose</td><td>Until you delete the account</td></tr>
<tr><td>Your credit balance and a ledger of each grant and spend: which AI page used credits, its style, and when</td><td>To give you the right credits, refund failed ones and handle disputes</td><td>Until you delete the account</td></tr>
<tr><td>The App Store transactions of your subscription (Apple's signed transaction: product, dates, transaction IDs, a renewal status; never your payment details or Apple Account)</td><td>To give your plan's credits once, renew them, and take them back if Apple refunds a purchase</td><td>Kept for accounting and to prevent abuse; on account deletion they are kept without your account ID</td></tr>
<tr><td>An identifier of your App Store account for this app (Apple's <em>appTransactionId</em>)</td><td>So the 30 free credits are given once per App Store account, not once per install</td><td>Kept without your account ID after deletion, for the same reason</td></tr>
</tbody>
</table></div>"""),
("ai", "4. AI pages", """<p>AI pages are made only after you allow it on the permission screen; you can withdraw that at any time in Profile → Use photos with AI, and the rest of the app, including Original pages, keeps working without it.</p>
<ul>
<li><strong>AI page</strong>: the photo, resized to at most 1536 pixels, is sent over an encrypted connection to Arista's server, which asks <strong>OpenAI</strong> to draw the coloring page.</li>
<li><strong>Kept at most two days.</strong> Arista's server keeps the photo and the finished page in private storage so that a page you paid for is never lost if the connection drops, and deletes them as soon as the app has them, or after two days at the latest.</li>
<li><strong>The AI services</strong> process pictures under their API terms. OpenAI does not use API data to train its models and may keep it for up to 30 days to detect abuse. Arista never uses your pictures to train AI.</li>
<li>Pictures may be checked by OpenAI's safety filters; a picture it refuses is not charged.</li>
<li><strong>Reporting a page.</strong> If an AI page comes out offensive or wrong, open it and choose Share → Report this page. It opens an email to us with the page attached; you choose whether to send it. We read every report and answer within 48 hours, and use what you send only to handle the report and improve the styles' safety, then delete it.</li>
</ul>"""),
("permissions", "5. Permissions", """<div class="sa-table"><table>
<thead><tr><th>Permission</th><th>When it is asked</th><th>How it is used</th></tr></thead>
<tbody>
<tr><td>Camera</td><td>When you take a photo in the app</td><td>Only to take the photo you want to turn into a page</td></tr>
<tr><td>Add to Photos</td><td>When you first save a page</td><td>Only to add your artwork to your library; Arista can't read your library. Photos you pick are chosen in Apple's picker, which gives the app only those photos</td></tr>
<tr><td>Notifications</td><td>When you first start a focus session</td><td>A notification made on your iPhone when the session ends; nothing goes to a push service</td></tr>
</tbody>
</table></div>"""),
("purchases", "6. Purchases", """<p>Subscriptions are sold only through Apple's In-App Purchase. Apple takes the payment; Arista never receives your payment details or your Apple Account. The app sends Arista's server the signed transaction Apple gives it, and Apple notifies the server of renewals and refunds, so your credits stay right. Manage or cancel subscriptions in Settings › Apple Account › Subscriptions; refunds are Apple's to give, at reportaproblem.apple.com.</p>"""),
("sharing", "7. Who processes data, and where", """<p>We <strong>never sell</strong> personal data and share it only with the services Arista needs to run:</p>
<ul>
<li><strong>Supabase</strong> (database, storage and server functions), in Singapore;</li>
<li><strong>OpenAI</strong>, USA: drawing AI pages;</li>
<li><strong>Apple</strong>: the App Store, purchases and their notifications;</li>
<li><strong>GitHub</strong> (GitHub Pages, USA) hosts this website.</li>
</ul>
<p>Data may therefore be processed outside your country, including in Singapore and the USA. We rely on these providers' contractual safeguards for such transfers, and follow the procedures that apply to an organisation of our size, including under Vietnam's Personal Data Protection Law (No. 91/2025/QH15).</p>"""),
("rights", "8. Your rights and deleting your data", f"""<ul>
<li><strong>In the app</strong>: Profile → Delete account deletes your account on Arista's server: your credits and ledger, and any stored pictures and pages. App Store transaction records are kept without your account ID, for accounting and to prevent abuse. A subscription is billed by Apple and keeps renewing until you cancel it; the app reminds you and opens Manage subscription.</li>
<li><strong>On your phone</strong>: delete artworks and collections in the app, or delete the app to remove everything stored in it.</li>
<li><strong>Anything else</strong>: you may ask to access, correct or delete your data, withdraw consent, or object to processing, under the GDPR, the UK GDPR, the CCPA, Vietnam's PDPL or other laws that apply to you. Write to <a href="mailto:{MAIL}?subject=Arista%20privacy">{MAIL}</a> with your account ID (shown in Profile); we reply within 15 days. You may also complain to your data protection authority.</li>
</ul>"""),
("security", "9. Security", """<p>Everything between the app and the server travels over encrypted connections. Each account can only reach its own data; pictures are kept in private storage reached only through short-lived links. Purchases are accepted only with Apple's signature, checked on the server. Only the developer can reach the server's data.</p>"""),
("website", "10. This website", """<p>The site sets no cookies and runs no analytics. It loads two typefaces from Google Fonts, so your browser fetches them from Google. Our host, GitHub, may keep technical logs such as IP addresses to run and secure the service, under its own policy.</p>"""),
("children", "11. Children", """<p>Arista is not directed at children under 13, and we do not knowingly collect personal information from them. It has no chat, no social features and no content visible to other people. Purchases need the permission of the Apple Account holder, and Apple's Ask to Buy works as usual.</p>"""),
("changes", "12. Changes", """<p>We publish new versions here with a new effective date, and in the app. If we want to use data for a new purpose, we will ask for your consent first.</p>"""),
],
},
"vi": {
"summary": """<p><strong>Tóm tắt:</strong> Arista không có quảng cáo, không có phân tích hành vi, không theo dõi, và không bao giờ hỏi tên, email hay mật khẩu của bạn. Ảnh, trang tô màu, bộ sưu tập và bảng màu nằm trên iPhone của bạn. Một bức ảnh chỉ rời điện thoại khi bạn tạo trang theo kiểu AI, và chỉ sau khi bạn cho phép: ảnh đi tới máy chủ của Arista rồi tới OpenAI để vẽ trang, và Arista giữ ảnh tối đa hai ngày. Để tính credit, Arista tạo cho điện thoại của bạn một tài khoản ẩn danh, bạn có thể xoá trong app ở Hồ sơ → Xoá tài khoản.</p>""",
"sections": [
("controller", "1. Ai chịu trách nhiệm", f"""<p>Arista (trên App Store với tên Arista Studio) do Ioniclabs làm, là nhà phát triển ghi trên trang App Store của app, và chịu trách nhiệm về dữ liệu mô tả ở đây. Liên hệ về quyền riêng tư: <a href="mailto:{MAIL}?subject=Arista">{MAIL}</a>.</p>
<p>Chính sách này áp dụng cho app Arista trên iPhone và trang web này.</p>"""),
("device", "2. Những gì nằm trên điện thoại của bạn", """<p>Ảnh bạn chụp hoặc nhập, các trang bạn tô, tác phẩm, bộ sưu tập, bảng màu, cài đặt tập trung và hồ sơ (tên và màu bạn chọn) được lưu trong app trên iPhone. Chúng nằm trong bản sao lưu iCloud hoặc máy tính nếu bạn dùng, và bị xoá khi bạn xoá app. Trang kiểu Original được vẽ hoàn toàn trên iPhone; không có gì được gửi đi.</p>"""),
("account", "3. Tài khoản ẩn danh của bạn", """<p>Lần đầu bạn mở Arista, app tạo một tài khoản ẩn danh trên máy chủ để tính credit và giao dịch. Bạn không bao giờ phải đăng nhập. Khoá của tài khoản được lưu trong keychain của iPhone, nên tài khoản vẫn còn sau khi xoá và cài lại app trên cùng điện thoại.</p>
<div class="sa-table"><table>
<thead><tr><th>Dữ liệu trên máy chủ của Arista</th><th>Để làm gì</th><th>Giữ bao lâu</th></tr></thead>
<tbody>
<tr><td>Một ID tài khoản ngẫu nhiên</td><td>Để biết credit nào của ai</td><td>Cho đến khi bạn xoá tài khoản</td></tr>
<tr><td>Số dư credit và sổ ghi từng lần cộng, trừ: trang AI nào đã dùng credit, kiểu của trang, và thời điểm</td><td>Để cấp đúng credit, hoàn credit khi lỗi và xử lý khiếu nại</td><td>Cho đến khi bạn xoá tài khoản</td></tr>
<tr><td>Giao dịch App Store của gói (giao dịch có chữ ký của Apple: sản phẩm, ngày, mã giao dịch, trạng thái gia hạn; không bao giờ có thông tin thanh toán hay Tài khoản Apple)</td><td>Để cấp credit của gói đúng một lần, gia hạn, và thu hồi nếu Apple hoàn tiền</td><td>Giữ để kế toán và chống lạm dụng; khi xoá tài khoản thì giữ mà không còn ID tài khoản</td></tr>
<tr><td>Một mã định danh tài khoản App Store của bạn cho app này (<em>appTransactionId</em> của Apple)</td><td>Để 30 credit tặng chỉ được cấp một lần cho mỗi tài khoản App Store, không phải mỗi lần cài</td><td>Giữ mà không còn ID tài khoản sau khi xoá, vì cùng lý do</td></tr>
</tbody>
</table></div>"""),
("ai", "4. Trang AI", """<p>Trang AI chỉ được tạo sau khi bạn cho phép ở màn hình xin quyền; bạn có thể rút lại bất cứ lúc nào ở Hồ sơ → Dùng ảnh với AI, và phần còn lại của app, kể cả trang Original, vẫn dùng được khi không cho phép.</p>
<ul>
<li><strong>Trang AI</strong>: ảnh được thu nhỏ còn tối đa 1536 pixel, gửi qua kết nối mã hoá tới máy chủ của Arista, máy chủ nhờ <strong>OpenAI</strong> vẽ trang tô màu.</li>
<li><strong>Giữ tối đa hai ngày.</strong> Máy chủ của Arista giữ ảnh và trang hoàn chỉnh trong kho riêng để trang bạn đã trả phí không bị mất khi mất kết nối, và xoá ngay khi app đã nhận, chậm nhất sau hai ngày.</li>
<li><strong>Các dịch vụ AI</strong> xử lý ảnh theo điều khoản API của họ. OpenAI không dùng dữ liệu API để huấn luyện mô hình và có thể giữ tối đa 30 ngày để phát hiện lạm dụng. Arista không bao giờ dùng ảnh của bạn để huấn luyện AI.</li>
<li>Ảnh có thể được bộ lọc an toàn của OpenAI kiểm tra; ảnh bị từ chối thì không bị tính credit.</li>
<li><strong>Báo cáo một trang.</strong> Nếu một trang AI bị phản cảm hoặc sai, hãy mở trang và chọn Chia sẻ → Báo cáo trang này. App mở một email gửi chúng tôi kèm trang đó; bạn quyết định có gửi hay không. Chúng tôi đọc mọi báo cáo và trả lời trong 48 giờ, chỉ dùng những gì bạn gửi để xử lý báo cáo và cải thiện độ an toàn của các kiểu vẽ, sau đó xoá.</li>
</ul>"""),
("permissions", "5. Quyền truy cập", """<div class="sa-table"><table>
<thead><tr><th>Quyền</th><th>Khi nào được hỏi</th><th>Dùng để làm gì</th></tr></thead>
<tbody>
<tr><td>Camera</td><td>Khi bạn chụp ảnh trong app</td><td>Chỉ để chụp bức ảnh bạn muốn biến thành trang</td></tr>
<tr><td>Thêm vào Ảnh</td><td>Lần đầu bạn lưu trang</td><td>Chỉ để thêm tác phẩm vào thư viện; Arista không đọc được thư viện. Ảnh bạn chọn được chọn qua bộ chọn của Apple, chỉ những ảnh đó đến được app</td></tr>
<tr><td>Thông báo</td><td>Lần đầu bạn bắt đầu một phiên tập trung</td><td>Một thông báo tạo ngay trên iPhone khi phiên kết thúc; không có gì gửi tới dịch vụ đẩy thông báo</td></tr>
</tbody>
</table></div>"""),
("purchases", "6. Giao dịch", """<p>Các gói chỉ được bán qua In-App Purchase của Apple. Apple nhận thanh toán; Arista không bao giờ nhận thông tin thanh toán hay Tài khoản Apple của bạn. App gửi tới máy chủ của Arista giao dịch có chữ ký mà Apple cấp, và Apple báo cho máy chủ khi gia hạn hoặc hoàn tiền, để credit của bạn luôn đúng. Quản lý hoặc huỷ gói ở Cài đặt › Tài khoản Apple › Đăng ký; hoàn tiền do Apple quyết định, tại reportaproblem.apple.com.</p>"""),
("sharing", "7. Ai xử lý dữ liệu, và ở đâu", """<p>Chúng tôi <strong>không bao giờ bán</strong> dữ liệu cá nhân và chỉ chia sẻ với các dịch vụ Arista cần để hoạt động:</p>
<ul>
<li><strong>Supabase</strong> (cơ sở dữ liệu, lưu trữ và hàm máy chủ), tại Singapore;</li>
<li><strong>OpenAI</strong>, Mỹ: vẽ trang AI;</li>
<li><strong>Apple</strong>: App Store, giao dịch và thông báo về giao dịch;</li>
<li><strong>GitHub</strong> (GitHub Pages, Mỹ) lưu trữ trang web này.</li>
</ul>
<p>Vì vậy dữ liệu có thể được xử lý ngoài Việt Nam, gồm Singapore và Mỹ. Chúng tôi dựa vào các cam kết theo hợp đồng của những nhà cung cấp này khi chuyển dữ liệu, và thực hiện các thủ tục áp dụng cho tổ chức có quy mô như chúng tôi, kể cả theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15.</p>"""),
("rights", "8. Quyền của bạn và xoá dữ liệu", f"""<ul>
<li><strong>Trong app</strong>: Hồ sơ → Xoá tài khoản xoá tài khoản của bạn trên máy chủ của Arista: credit và sổ credit, cùng mọi ảnh và trang đang lưu. Bản ghi giao dịch App Store được giữ mà không còn ID tài khoản, để kế toán và chống lạm dụng. Gói do Apple tính phí và vẫn tự gia hạn cho đến khi bạn huỷ; app nhắc bạn và mở Quản lý gói.</li>
<li><strong>Trên điện thoại</strong>: xoá tác phẩm và bộ sưu tập trong app, hoặc xoá app để xoá mọi thứ lưu trong đó.</li>
<li><strong>Yêu cầu khác</strong>: bạn có quyền yêu cầu xem, sửa hoặc xoá dữ liệu, rút lại sự đồng ý, hoặc phản đối việc xử lý, theo Luật Bảo vệ dữ liệu cá nhân, GDPR, CCPA hoặc luật khác áp dụng với bạn. Viết tới <a href="mailto:{MAIL}?subject=Arista%20privacy">{MAIL}</a> kèm ID tài khoản (hiện trong Hồ sơ); chúng tôi trả lời trong 15 ngày. Bạn cũng có thể khiếu nại tới cơ quan bảo vệ dữ liệu.</li>
</ul>"""),
("security", "9. Bảo mật", """<p>Mọi dữ liệu giữa app và máy chủ đi qua kết nối mã hoá. Mỗi tài khoản chỉ truy cập được dữ liệu của chính mình; ảnh được giữ trong kho riêng, chỉ mở được qua đường dẫn ngắn hạn. Giao dịch chỉ được chấp nhận khi có chữ ký của Apple, được kiểm tra trên máy chủ. Chỉ nhà phát triển truy cập được dữ liệu trên máy chủ.</p>"""),
("website", "10. Trang web này", """<p>Trang web không đặt cookie và không chạy công cụ phân tích. Trang tải hai phông chữ từ Google Fonts, nên trình duyệt của bạn lấy chúng từ Google. Đơn vị lưu trữ, GitHub, có thể ghi nhật ký kỹ thuật như địa chỉ IP để vận hành và bảo vệ dịch vụ, theo chính sách của họ.</p>"""),
("children", "11. Trẻ em", """<p>Arista không hướng tới trẻ em dưới 13 tuổi, và chúng tôi không cố ý thu thập thông tin cá nhân của trẻ. App không có trò chuyện, tính năng mạng xã hội hay nội dung người khác xem được. Giao dịch cần sự cho phép của chủ Tài khoản Apple, và tính năng Ask to Buy của Apple vẫn hoạt động như thường.</p>"""),
("changes", "12. Thay đổi", """<p>Chúng tôi đăng phiên bản mới tại đây kèm ngày hiệu lực mới, và trong app. Nếu muốn dùng dữ liệu cho mục đích mới, chúng tôi sẽ xin sự đồng ý của bạn trước.</p>"""),
],
},
}

# ---------------------------------------------------------------- terms of use

TERMS = {
"en": {
"summary": """<p><strong>In short:</strong> coloring, Original pages and the focus timer are free. AI pages use credits, which come with your plan or the free welcome gift. Credits have no cash value and end when your plan ends. Upload only pictures you have the right to use; what you make is yours. Purchases go through Apple, and refunds are Apple's to give.</p>""",
"sections": [
("agreement", "1. The agreement", """<p>Arista (on the App Store as Arista Studio, “the App”) is made and published by Ioniclabs, the developer named as the seller on the App's App Store page (“we”, “us”). These Terms of Use are the agreement between you and us for your use of the App. They supplement Apple's Licensed Application End User License Agreement where it applies; where they conflict on a matter Apple's terms require, Apple's terms prevail.</p>
<p>The agreement is between you and us only, not with Apple. Apple is not responsible for the App or its content. By downloading or using the App you accept these terms; if you do not, do not use the App and delete it.</p>"""),
("licence", "2. Your licence", """<p>We grant you a personal, non-exclusive, non-transferable, revocable licence to use the App on Apple-branded devices you own or control, as allowed by the Usage Rules of the Apple Media Services Terms and Conditions.</p>
<p>You may not copy, redistribute, sell, rent or sublicense the App; reverse-engineer it except where the law expressly allows; interfere with its server or use it, or its credits, through anything but the App itself; or use it to break the law or anyone's rights. The App, its name, artwork, styles and code remain ours.</p>"""),
("credits", "3. Credits", """<ul>
<li>AI pages use credits: at present 10 for an AI page. The App shows the cost before you start. We may change costs or add features with their own cost; a change never takes credits you already have.</li>
<li>Every App Store account gets 30 credits once, to try the AI. Plans include credits each month (section 4).</li>
<li>Credits are reserved when you start and are given back automatically if the AI fails, times out, refuses the picture, or you cancel before it finishes.</li>
<li>Credits have no cash value, cannot be bought separately, exchanged, transferred or sold, and are not refundable by us. They belong to the anonymous account on your phone; deleting the account deletes them.</li>
<li>We may remove credits obtained through fraud, abuse of refunds, a fault in the App or a refunded purchase.</li>
</ul>"""),
("plans", "4. Plans and paying for them", """<p>Arista MAX and Arista ULTRA are auto-renewable subscriptions sold only through Apple's In-App Purchase. Apple takes the payment and holds the billing relationship.</p>
<ul>
<li><strong>MAX</strong>: monthly or annual, 600 credits every month (an annual plan gives them month by month). <strong>ULTRA</strong>: monthly, 2,000, 4,000 or 8,000 credits a month. MAX also unlocks pencil, pen and every palette.</li>
<li>Unused plan credits roll over while the plan is active, up to three months of its allowance; above that, the oldest are dropped first. When the plan ends (cancelled, expired or refunded), its credits end with it. The welcome credits do not expire.</li>
<li>Changing plans: moving up to a larger plan applies at once and keeps your balance; Apple refunds the unused part of the old plan. Moving down, or between monthly and annual MAX, applies at your next renewal, when the balance is trimmed to the new plan's limit.</li>
<li>A subscription renews automatically at the end of each period unless cancelled at least 24 hours before it ends. Manage or cancel it in Settings › Apple Account › Subscriptions.</li>
<li>Refunds are Apple's to give, at reportaproblem.apple.com. If Apple refunds a purchase, the credits it gave are taken back.</li>
<li>We may change prices; a change reaches you only through Apple, with the notice and the choice to cancel that Apple requires.</li>
</ul>"""),
("content", "5. Your pictures and what you make", """<ul>
<li>Use only photos and pictures that you took, own, or have permission to use, and get the consent of the people in them before turning them into pages.</li>
<li>Do not use the App to make content that is sexual, that involves minors in any inappropriate way, that harasses or impersonates real people, that is hateful or violent, or that infringes anyone's rights. The AI services' safety filters may refuse a picture; refused pictures are not charged.</li>
<li>If an AI page comes out offensive or wrong, report it from the page (Share → Report this page) or by email. We answer reports within 48 hours and may suspend the AI features of an account that misuses them.</li>
<li>What you make in the App is yours. We claim no ownership of your photos or pages, and we never use them to train AI. You are responsible for how you use and share them.</li>
<li>AI output is made by third-party models (OpenAI). It can be imperfect, unexpected or similar to other people's output, and it may not be protected by copyright everywhere. Pages are for your personal, non-commercial use unless the law where you are allows more.</li>
</ul>"""),
("service", "6. The service", """<p>The AI features need an internet connection and our server and third-party services, which may be unavailable at times. We may add, change or remove features, styles or models, and may stop the AI service; if we stop it while you have a paid plan, we will tell you in advance and stop renewals. Coloring, Original pages and your artworks keep working on your phone without the server.</p>"""),
("support", "7. Support", f"""<p>Support is ours to provide, not Apple's: Apple has no obligation to furnish any maintenance or support services for the App. Write to <a href="mailto:{MAIL}?subject=Arista">{MAIL}</a>.</p>"""),
("warranty", "8. No warranty", """<p>To the fullest extent the law allows, the App is provided “as is” and “as available”, without warranty of any kind, express or implied, including merchantability, fitness for a particular purpose and non-infringement. In the event of any failure of the App to conform to any warranty that does apply, you may notify Apple, and Apple will refund the purchase price of the App to you; to the maximum extent permitted by law, Apple has no other warranty obligation with respect to the App. Your mandatory consumer rights are unaffected.</p>"""),
("liability", "9. Limitation of liability", """<p>To the fullest extent the law allows, we are not liable for indirect, incidental, special or consequential damages, or for lost data or profit, arising out of your use of the App. Our total liability for any claim is limited to what you paid for the App and its subscriptions in the twelve months before the claim. Nothing here limits liability that cannot be limited by law.</p>"""),
("claims", "10. Product and intellectual-property claims", """<p>We, not Apple, are responsible for addressing any claim by you or a third party relating to the App or your possession and use of it, including product-liability claims, claims that the App fails to conform to a legal or regulatory requirement, and claims under consumer-protection, privacy or similar law. If a third party claims the App infringes their intellectual property, we, not Apple, are solely responsible for its investigation, defence, settlement and discharge.</p>"""),
("apple", "11. Apple, third-party terms and export", """<p>You must comply with applicable third-party terms when using the App, including Apple's. Apple and its subsidiaries are third-party beneficiaries of these terms and, once you accept them, have the right to enforce them against you. You represent that you are not located in a country subject to a U.S. Government embargo or designated as a “terrorist supporting” country, and are not on any U.S. Government list of prohibited or restricted parties.</p>"""),
("ending", "12. Ending it", """<p>You may end this agreement at any time by deleting your account in the App and deleting the App; cancel any subscription with Apple. We may suspend the AI features or end your licence if you materially breach these terms, for example by abusing the service or its credits.</p>"""),
("law", "13. Governing law", """<p>These terms are governed by the laws of Vietnam, and the courts of Vietnam have jurisdiction, except where the mandatory law of your country of residence gives you different rights or a different forum as a consumer; those rights stand.</p>"""),
("changes", "14. Changes", f"""<p>We may update these terms as the App or the law changes. The effective date at the top changes with them, and the current version is always at this address. Continuing to use the App after a change means you accept it. Questions: <a href="mailto:{MAIL}?subject=Arista">{MAIL}</a>.</p>"""),
],
},
"vi": {
"summary": """<p><strong>Tóm tắt:</strong> tô màu, trang Original và đồng hồ tập trung miễn phí. Trang AI dùng credit, có trong gói hoặc trong quà chào mừng. Credit không có giá trị quy đổi tiền và hết khi gói hết. Chỉ tải lên ảnh bạn có quyền sử dụng; những gì bạn tạo ra là của bạn. Giao dịch qua Apple, và hoàn tiền do Apple quyết định.</p>""",
"sections": [
("agreement", "1. Thoả thuận", """<p>Arista (trên App Store với tên Arista Studio, “App”) do Ioniclabs làm và phát hành, là nhà phát triển ghi là người bán trên trang App Store của App (“chúng tôi”). Điều khoản này là thoả thuận giữa bạn và chúng tôi về việc dùng App. Điều khoản bổ sung cho Thoả thuận cấp phép người dùng cuối của Apple (Licensed Application EULA) khi áp dụng; nếu mâu thuẫn ở điểm mà điều khoản của Apple yêu cầu, điều khoản của Apple được ưu tiên.</p>
<p>Thoả thuận chỉ giữa bạn và chúng tôi, không phải với Apple. Apple không chịu trách nhiệm về App hay nội dung của App. Khi tải hoặc dùng App, bạn chấp nhận điều khoản này; nếu không đồng ý, đừng dùng App và hãy xoá nó.</p>"""),
("licence", "2. Giấy phép của bạn", """<p>Chúng tôi cấp cho bạn giấy phép cá nhân, không độc quyền, không chuyển nhượng, có thể thu hồi để dùng App trên thiết bị Apple bạn sở hữu hoặc kiểm soát, theo Quy tắc sử dụng trong Điều khoản dịch vụ Apple Media Services.</p>
<p>Bạn không được sao chép, phân phối lại, bán, cho thuê hay cấp phép lại App; dịch ngược App trừ khi luật cho phép rõ ràng; can thiệp vào máy chủ của App hoặc dùng App hay credit qua bất cứ thứ gì ngoài chính App; hoặc dùng App để vi phạm pháp luật hay quyền của người khác. App, tên, hình ảnh, các kiểu vẽ và mã nguồn vẫn thuộc về chúng tôi.</p>"""),
("credits", "3. Credit", """<ul>
<li>Trang AI dùng credit: hiện là 10 cho một trang AI. App hiện chi phí trước khi bạn bắt đầu. Chúng tôi có thể đổi chi phí hoặc thêm tính năng có chi phí riêng; thay đổi không bao giờ lấy đi credit bạn đang có.</li>
<li>Mỗi tài khoản App Store được tặng 30 credit một lần để dùng thử AI. Các gói có credit mỗi tháng (mục 4).</li>
<li>Credit được giữ lại khi bạn bắt đầu và tự động hoàn lại nếu AI lỗi, quá thời gian, từ chối bức ảnh, hoặc bạn huỷ trước khi xong.</li>
<li>Credit không có giá trị quy đổi tiền, không bán riêng, không đổi, chuyển nhượng hay bán lại được, và chúng tôi không hoàn tiền cho credit. Credit thuộc tài khoản ẩn danh trên điện thoại của bạn; xoá tài khoản thì credit bị xoá.</li>
<li>Chúng tôi có thể thu hồi credit có được do gian lận, lạm dụng hoàn credit, lỗi của App hoặc giao dịch đã được hoàn tiền.</li>
</ul>"""),
("plans", "4. Gói và thanh toán", """<p>Arista MAX và Arista ULTRA là gói đăng ký tự gia hạn, chỉ bán qua In-App Purchase của Apple. Apple nhận thanh toán và quản lý việc tính phí.</p>
<ul>
<li><strong>MAX</strong>: theo tháng hoặc theo năm, 600 credit mỗi tháng (gói năm cấp theo từng tháng). <strong>ULTRA</strong>: theo tháng, 2.000, 4.000 hoặc 8.000 credit mỗi tháng. MAX còn mở bút chì, bút mực và mọi bảng màu.</li>
<li>Credit của gói chưa dùng được cộng dồn khi gói còn hiệu lực, tối đa bằng ba tháng hạn mức; vượt mức đó thì credit cũ nhất bị bỏ trước. Khi gói kết thúc (huỷ, hết hạn hoặc được hoàn tiền), credit của gói kết thúc theo. Credit chào mừng không hết hạn.</li>
<li>Đổi gói: lên gói lớn hơn có hiệu lực ngay và giữ số dư; Apple hoàn phần chưa dùng của gói cũ. Xuống gói nhỏ hơn, hoặc đổi giữa MAX tháng và năm, có hiệu lực từ kỳ gia hạn tới, khi đó số dư được cắt về mức tối đa của gói mới.</li>
<li>Gói tự gia hạn khi hết mỗi kỳ trừ khi huỷ ít nhất 24 giờ trước khi kỳ kết thúc. Quản lý hoặc huỷ ở Cài đặt › Tài khoản Apple › Đăng ký.</li>
<li>Hoàn tiền do Apple quyết định, tại reportaproblem.apple.com. Nếu Apple hoàn tiền một giao dịch, credit giao dịch đó cấp sẽ bị thu hồi.</li>
<li>Chúng tôi có thể đổi giá; thay đổi chỉ đến với bạn qua Apple, kèm thông báo và quyền huỷ mà Apple yêu cầu.</li>
</ul>"""),
("content", "5. Ảnh của bạn và những gì bạn tạo", """<ul>
<li>Chỉ dùng ảnh do bạn chụp, sở hữu hoặc được phép sử dụng, và xin sự đồng ý của người có trong ảnh trước khi biến ảnh thành trang.</li>
<li>Không dùng App để tạo nội dung khiêu dâm, nội dung liên quan đến trẻ vị thành niên theo cách không phù hợp, quấy rối hay mạo danh người thật, kích động thù ghét hay bạo lực, hoặc xâm phạm quyền của người khác. Bộ lọc an toàn của các dịch vụ AI có thể từ chối một bức ảnh; ảnh bị từ chối không bị tính credit.</li>
<li>Nếu một trang AI bị phản cảm hoặc sai, hãy báo cáo ngay từ trang đó (Chia sẻ → Báo cáo trang này) hoặc qua email. Chúng tôi trả lời báo cáo trong 48 giờ và có thể tạm dừng tính năng AI của tài khoản dùng sai mục đích.</li>
<li>Những gì bạn tạo trong App là của bạn. Chúng tôi không nhận quyền sở hữu ảnh hay trang của bạn, và không dùng chúng để huấn luyện AI. Bạn chịu trách nhiệm về cách bạn dùng và chia sẻ chúng.</li>
<li>Kết quả AI do mô hình của bên thứ ba tạo (OpenAI). Kết quả có thể chưa hoàn hảo, bất ngờ hoặc giống kết quả của người khác, và có thể không được bảo hộ bản quyền ở mọi nơi. Trang dùng cho mục đích cá nhân, phi thương mại, trừ khi luật nơi bạn sống cho phép nhiều hơn.</li>
</ul>"""),
("service", "6. Dịch vụ", """<p>Các tính năng AI cần kết nối internet, máy chủ của chúng tôi và dịch vụ của bên thứ ba, nên đôi lúc có thể không dùng được. Chúng tôi có thể thêm, đổi hoặc bỏ tính năng, kiểu vẽ hay mô hình, và có thể ngừng dịch vụ AI; nếu ngừng khi bạn đang có gói trả phí, chúng tôi sẽ báo trước và ngừng gia hạn. Tô màu, trang Original và tác phẩm của bạn vẫn hoạt động trên điện thoại mà không cần máy chủ.</p>"""),
("support", "7. Hỗ trợ", f"""<p>Việc hỗ trợ là của chúng tôi, không phải của Apple: Apple không có nghĩa vụ cung cấp dịch vụ bảo trì hay hỗ trợ nào cho App. Viết tới <a href="mailto:{MAIL}?subject=Arista">{MAIL}</a>.</p>"""),
("warranty", "8. Không bảo đảm", """<p>Trong phạm vi tối đa pháp luật cho phép, App được cung cấp “nguyên trạng” và “tuỳ khả năng”, không kèm bảo đảm nào, rõ ràng hay ngụ ý, kể cả về khả năng thương mại, sự phù hợp cho mục đích cụ thể và không vi phạm. Nếu App không đáp ứng một bảo đảm có áp dụng, bạn có thể báo Apple, và Apple sẽ hoàn lại giá mua App; trong phạm vi tối đa pháp luật cho phép, Apple không có nghĩa vụ bảo đảm nào khác đối với App. Quyền bắt buộc của người tiêu dùng không bị ảnh hưởng.</p>"""),
("liability", "9. Giới hạn trách nhiệm", """<p>Trong phạm vi tối đa pháp luật cho phép, chúng tôi không chịu trách nhiệm về thiệt hại gián tiếp, ngẫu nhiên, đặc biệt hay hệ quả, hoặc mất dữ liệu hay lợi nhuận, phát sinh từ việc bạn dùng App. Tổng trách nhiệm của chúng tôi cho mọi khiếu nại giới hạn ở số tiền bạn đã trả cho App và các gói trong mười hai tháng trước khiếu nại. Không điều nào ở đây giới hạn trách nhiệm mà pháp luật không cho phép giới hạn.</p>"""),
("claims", "10. Khiếu nại về sản phẩm và sở hữu trí tuệ", """<p>Chúng tôi, không phải Apple, chịu trách nhiệm giải quyết mọi khiếu nại của bạn hoặc bên thứ ba liên quan đến App hoặc việc bạn sở hữu và dùng App, gồm khiếu nại về trách nhiệm sản phẩm, về việc App không tuân thủ quy định pháp luật, và khiếu nại theo luật bảo vệ người tiêu dùng, quyền riêng tư hoặc tương tự. Nếu bên thứ ba cho rằng App xâm phạm quyền sở hữu trí tuệ của họ, chúng tôi, không phải Apple, hoàn toàn chịu trách nhiệm điều tra, bảo vệ, giải quyết và xử lý khiếu nại đó.</p>"""),
("apple", "11. Apple, điều khoản bên thứ ba và xuất khẩu", """<p>Bạn phải tuân thủ điều khoản của bên thứ ba khi dùng App, gồm điều khoản của Apple. Apple và các công ty con là bên thụ hưởng thứ ba của điều khoản này và, khi bạn chấp nhận, có quyền thực thi điều khoản đối với bạn. Bạn cam kết không ở quốc gia bị Chính phủ Mỹ cấm vận hoặc xếp vào danh sách “hỗ trợ khủng bố”, và không có tên trong danh sách bị cấm hay hạn chế nào của Chính phủ Mỹ.</p>"""),
("ending", "12. Chấm dứt", """<p>Bạn có thể chấm dứt thoả thuận bất cứ lúc nào bằng cách xoá tài khoản trong App và xoá App; huỷ gói với Apple. Chúng tôi có thể tạm dừng các tính năng AI hoặc chấm dứt giấy phép của bạn nếu bạn vi phạm nghiêm trọng điều khoản này, ví dụ lạm dụng dịch vụ hay credit.</p>"""),
("law", "13. Luật áp dụng", """<p>Điều khoản này theo pháp luật Việt Nam, và toà án Việt Nam có thẩm quyền, trừ khi luật bắt buộc nơi bạn cư trú cho bạn quyền khác hoặc nơi giải quyết khác với tư cách người tiêu dùng; các quyền đó vẫn được giữ.</p>"""),
("changes", "14. Thay đổi", f"""<p>Chúng tôi có thể cập nhật điều khoản khi App hoặc pháp luật thay đổi. Ngày hiệu lực ở đầu trang thay đổi theo, và phiên bản hiện hành luôn ở địa chỉ này. Tiếp tục dùng App sau khi thay đổi nghĩa là bạn chấp nhận. Câu hỏi: <a href="mailto:{MAIL}?subject=Arista">{MAIL}</a>.</p>"""),
],
},
}

# ---------------------------------------------------------------- templates

def head(t, title, desc, up, og_url):
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Generated by tools/make_arista.py. Edit the text there and run it again. -->
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" sizes="64x64" href="{up}assets/arista/favicon-64.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://ioniclabs.app/assets/arista/icon.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ioniclabs.app/{og_url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/{CSS}">
<script src="{up}assets/site.js?v=1" defer></script>
</head>
<body>
"""


def lang_menu(lang, en_href, vi_href):
    return f"""<details class="lang">
    <summary>{T[lang]['label']}</summary>
    <div class="lang-menu">
      <a href="{en_href}"{' aria-current="page"' if lang == 'en' else ''}>English</a>
      <a href="{vi_href}"{' aria-current="page"' if lang == 'vi' else ''}>Tiếng Việt</a>
    </div>
  </details>"""


def prefix(lang):
    """Path from apps/arista/ (or vi/apps/arista/) up to the site root."""
    return "../../" if lang == "en" else "../../../"


def app_page(lang):
    t = T[lang]
    up = prefix(lang)
    other = "../../vi/apps/arista/" if lang == "en" else "../../../apps/arista/"
    en_href, vi_href = ("./", other) if lang == "en" else (other, "./")
    cards = "\n".join(
        f'<div class="card"><div class="card-head"><span aria-hidden="true" class="sa-icon">{i}</span><h3>{h}</h3></div><p>{p}</p></div>'
        for i, h, p in t["cards"])
    shots = "\n".join(
        f'      <figure><img src="{up}assets/arista/shots/{n}.jpg?v={SHOTS_V}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
        for n, alt, cap in t["shots"])
    og = "apps/arista/" if lang == "en" else "vi/apps/arista/"
    return head(t, t["title"], t["desc"], up, og) + f"""<nav class="ap-nav">
  <img class="icon" src="{up}assets/arista/icon.png" alt="">
  <a class="here" href="./">Arista</a>
  <span class="bar"></span>
  <a class="hide-sm" href="./#pricing">{'Pricing' if lang == 'en' else 'Giá'}</a>
  <a class="hide-sm" href="privacy/">{t['privacy']}</a>
  <a class="hide-sm" href="terms/">{t['terms']}</a>
  {lang_menu(lang, en_href, vi_href)}
  <a class="cta" href="mailto:{MAIL}?subject=Arista">{t['support']}</a>
</nav>

<main class="ap sa">
  <section class="ap-hero ap-head">
    <span class="ap-eyebrow">{t['eyebrow']}</span>
    <h1 class="ap-display">{t['display']}</h1>
    <p class="ap-sub">{t['sub']}</p>
    <p class="ap-sub"><span class="tag tag--soon">{t['soon']}</span>&nbsp; {t['soon_p']}</p>
    <div class="ap-stage">
      <img src="{up}assets/arista/shots/3-coloring.jpg?v={SHOTS_V}" alt="{t['hero_alt']}">
    </div>
  </section>

  <section id="screens" class="ap-head">
    <h2 class="ap-display">{t['screens']}</h2>
    <p class="ap-sub">{t['screens_sub']}</p>
    <div class="ap-row">
{shots}
    </div>
  </section>

  <section class="ap-head">
    <h2 class="ap-display">{t['inside']}</h2>
    <div class="ap-cards">
{cards}
</div>
  </section>

  <section id="pricing" class="ap-head">
    <h2 class="ap-display">{t['pricing']}</h2>
    <p class="ap-sub">{t['pricing_sub']}</p>
    <div class="ap-cards">
      <div class="card">
        <div class="card-head"><h3>MAX</h3></div>
        <p class="price">$9.99 <small>{'a month · or $69.99 a year' if lang == 'en' else 'mỗi tháng · hoặc $69.99 mỗi năm'}</small></p>
        <p>{t['max_p']}</p>
      </div>
      <div class="card">
        <div class="card-head"><h3>ULTRA</h3></div>
        <p class="price">{'from' if lang == 'en' else 'từ'} $24.99 <small>{'a month' if lang == 'en' else 'mỗi tháng'}</small></p>
        <ul><li><strong>2,000</strong> · $24.99</li><li><strong>4,000</strong> · $44.99</li><li><strong>8,000</strong> · $79.99</li></ul>
        <p>{t['ultra_p']}</p>
      </div>
    </div>
    <div class="sa-body"><p class="sa-small sa-muted" style="margin-top:18px">{t['plans_note']}</p></div>
  </section>

  <section class="ap-head">
    <div class="ap-cards">
<a class="card" href="privacy/"><div class="card-head"><h3>{t['privacy']}</h3></div><p>{t['privacy_card']}</p><span class="sa-more">{t['more_privacy']}</span></a>
<a class="card" href="terms/"><div class="card-head"><h3>{t['terms']}</h3></div><p>{t['terms_card']}</p><span class="sa-more">{t['more_terms']}</span></a>
</div>
  </section>

  <footer class="ap-foot">
    <div class="cols">
      <div>
        <div class="sign"><img src="{up}assets/arista/icon.png" alt="">Arista</div>
        <p class="fine" style="margin-top:14px;max-width:30ch">{t['foot']}</p>
      </div>
      <div>
        <h4>Arista</h4>
        <ul>
          <li><a href="./">{t['home']}</a></li>
          <li><a href="mailto:{MAIL}?subject=Arista">{t['support']}</a></li>
        </ul>
      </div>
      <div>
        <h4>{'Legal' if lang == 'en' else 'Pháp lý'}</h4>
        <ul>
          <li><a href="privacy/">{t['privacy']}</a></li>
          <li><a href="terms/">{t['terms']}</a></li>
        </ul>
      </div>
      <div>
        <h4>Ioniclabs</h4>
        <ul>
          <li><a href="{up}{'' if lang == 'en' else 'vi/'}">{t['all_apps']}</a></li>
          <li><a href="{other}">{t['lang_other']}</a></li>
        </ul>
      </div>
    </div>
    <p class="fine">{t['fine']}</p>
    <p class="fine" style="margin-top:8px">Arista © 2026 Ioniclabs</p>
  </footer>

</main>
</body>
</html>
"""


def doc_page(lang, kind):
    t = T[lang]
    doc = (PRIVACY if kind == "privacy" else TERMS)[lang]
    up = prefix(lang) + "../"
    name = t[kind]
    other = f"../../../vi/apps/arista/{kind}/" if lang == "en" else f"../../../../apps/arista/{kind}/"
    en_href, vi_href = ("./", other) if lang == "en" else (other, "./")
    words = name.split(" ")
    h1 = " ".join(words[:-1]) + f" <mark>{words[-1]}</mark>"
    eff = ("Effective " if lang == "en" else "Hiệu lực ") + EFFECTIVE[lang]
    binding = (" · The English version is the binding one; the Vietnamese one is a translation."
               if lang == "en" else " · Bản tiếng Anh là bản có giá trị ràng buộc; bản tiếng Việt là bản dịch.")
    toc = "".join(f'<li><a href="#{i}">{h}</a></li>' for i, h, _ in doc["sections"])
    body = "\n".join(f'<h2 id="{i}">{h}</h2>\n{b}' for i, h, b in doc["sections"])
    desc = ("What Arista keeps, where, why, who processes it and how to delete it." if kind == "privacy" and lang == "en"
            else "Arista lưu gì, ở đâu, vì sao, ai xử lý và cách xoá." if kind == "privacy"
            else "The terms for Arista: credits, plans, what you may make with the AI and the licence." if lang == "en"
            else "Điều khoản của Arista: credit, gói, những gì bạn được tạo bằng AI và giấy phép.")
    og = ("" if lang == "en" else "vi/") + f"apps/arista/{kind}/"
    other_doc = "terms" if kind == "privacy" else "privacy"
    return head(t, f"{name} — Arista", desc, up, og) + f"""<div class="wrap">

  <header class="legal-top">
    <div class="legal-top-row">
      <a class="brand" href="../"><img src="{up}assets/arista/icon.png" alt="">Arista</a>
      {lang_menu(lang, en_href, vi_href)}
    </div>
    <a class="mail" href="mailto:{MAIL}?subject=Arista">{MAIL} ↗</a>
  </header>

  <h1 class="h1-page">{h1}</h1>
  <div class="prose sa-doc">
    <p class="updated">{eff}{binding}</p>
    <details class="sa-toc"><summary>{t['contents']}</summary><ol>{toc}</ol></details>
    <div class="sa-note sa-ok">
{doc['summary']}
</div>
{body}
  </div>

  <footer>
    <nav>
      <a href="../">Arista</a>
      <span class="sep">|</span>
      <a href="{up}{'' if lang == 'en' else 'vi/'}">Ioniclabs</a>
      <span class="sep">|</span>
      <a href="../{other_doc}/">{t[other_doc]}</a>
      <span class="sep">|</span>
      <a href="mailto:{MAIL}?subject=Arista">{t['support']}</a>
    </nav>
    Arista © 2026 Ioniclabs
  </footer>

</div>
</body>
</html>
"""


SHORT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arista</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://ioniclabs.app/apps/arista/">
<meta property="og:title" content="Arista — photos into coloring pages">
<meta property="og:description" content="Your photos, ready to color.">
<meta property="og:image" content="https://ioniclabs.app/assets/arista/icon.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ioniclabs.app/apps/arista/">
<!-- The short link ioniclabs.app/arista. Generated by tools/make_arista.py. -->
<script>location.replace("../apps/arista/");</script>
<meta http-equiv="refresh" content="0; url=../apps/arista/">
</head>
<body>
<p><a href="../apps/arista/">Arista</a> · <a href="../vi/apps/arista/">Tiếng Việt</a></p>
</body>
</html>
"""


def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    for lang, base in (("en", "apps/arista"), ("vi", "vi/apps/arista")):
        write(f"{base}/index.html", app_page(lang))
        write(f"{base}/privacy/index.html", doc_page(lang, "privacy"))
        write(f"{base}/terms/index.html", doc_page(lang, "terms"))
    write("arista/index.html", SHORT)
