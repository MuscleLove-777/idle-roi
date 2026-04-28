"""放置ゲーム時給ランキング - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "放置ゲーム時給ランキング"
BLOG_DESCRIPTION = "「1時間放置で何円相当のジェム/通貨が貯まるか」を独自指標で実測。ROIランキングと周回最適化テンプレで、効率厨向けの定量比較メディア。"
BLOG_URL = "https://musclelove-777.github.io/idle-roi/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/idle-roi"

TARGET_CATEGORIES = [
    "時給ランキング月次更新",
    "無課金ROI比較",
    "課金効率ランキング",
    "周回最適化テンプレ",
    "新作放置ゲー初動レビュー",
    "オフライン報酬比較",
    "イベント期間限定ROI",
]

THEME = {
    "primary": "#0f3057",
    "accent": "#2e8b57",
    "gradient_start": "#0f3057",
    "gradient_end": "#2e8b57",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
