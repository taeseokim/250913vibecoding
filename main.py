# app.py
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(page_title="MBTI Top 10 by Country", layout="wide")
st.title("MBTI 유형별 비율 상위 10개 국가 시각화")
st.caption("동일 폴더의 countriesMBTI_16types.csv를 읽어옵니다. (Country + 16 MBTI 컬럼, 값은 0~1 비율)")

CSV_NAME = "countriesMBTI_16types.csv"
csv_path = Path(__file__).parent / CSV_NAME

@st.cache_data
def load_df(path: Path):
    df = pd.read_csv(path)
    return df

def validate_df(df: pd.DataFrame):
    if "Country" not in df.columns:
        st.error("❌ 'Country' 열이 없습니다. (국가명을 담은 'Country' 열이 필요합니다.)")
        return None

    mbti_cols = [
        "INFJ","ISFJ","INTP","ISFP","ENTP","INFP","ENTJ","ISTP",
        "INTJ","ESFP","ESTJ","ENFP","ESTP","ISTJ","ENFJ","ESFJ"
    ]
    missing = [c for c in mbti_cols if c not in df.columns]
    if missing:
        st.error(f"❌ 다음 MBTI 열이 누락되었습니다: {missing}")
        return None

    for c in mbti_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    if df[mbti_cols].isnull().any().any():
        st.warning("⚠️ 일부 MBTI 값이 숫자가 아닙니다. NaN은 0으로 대체합니다.")
        df[mbti_cols] = df[mbti_cols].fillna(0)

    return df, mbti_cols

def top10_chart(df: pd.DataFrame, col: str):
    top10 = (
        df[["Country", col]]
        .sort_values(col, ascending=False)
        .head(10)
        .copy()
    )
    top10["rank"] = range(1, len(top10) + 1)
    top10["percent"] = (top10[col] * 100).round(2)

    highlight = alt.selection_point(fields=["Country"], on="mouseover", nearest=True)

    bars = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(f"{col}:Q", title=f"{col} 비율"),
            y=alt.Y("Country:N", sort="-x", title="국가"),
            tooltip=[
                alt.Tooltip("rank:O", title="순위"),
                alt.Tooltip("Country:N", title="국가"),
                alt.Tooltip(f"{col}:Q", title="비율(0~1)"),
                alt.Tooltip("percent:Q", title="비율(%)"),
            ],
            opacity=alt.condition(highlight, alt.value(1), alt.value(0.6)),
        )
        .add_params(highlight)
    )

    text = (
        alt.Chart(top10)
        .mark_text(align="left", dx=3)
        .encode(
            x=alt.X(f"{col}:Q"),
            y=alt.Y("Country:N", sort="-x"),
            text=alt.Text("percent:Q", format=".2f"),
        )
    )

    return (bars + text).properties(
        width=700, height=380, title=f"{col} 상위 10개 국가"
    ).interactive()

# -------- Run --------
if not csv_path.exists():
    st.error(f"❌ CSV 파일을 찾을 수 없습니다: {csv_path.name}\n"
             "동일 폴더에 파일을 두고 다시 실행하세요.")
    st.stop()

df_raw = load_df(csv_path)
validated = validate_df(df_raw)
if not validated:
    st.stop()
df, mbti_cols = validated

with st.sidebar:
    st.header("옵션")
    selected_types = st.multiselect(
        "그래프로 볼 MBTI 유형 선택 (복수 선택 가능)",
        options=mbti_cols,
        default=["INFJ"]
    )
    show_quality = st.checkbox("데이터 품질 점검 보기", value=False)

if show_quality:
    st.subheader("데이터 품질 점검")
    st.write("행/열:", df.shape)
    sum_series = df[mbti_cols].sum(axis=1)
    st.write("국가별 16유형 합계 상위 5개(참고)")
    st.dataframe(
        pd.DataFrame({"Country": df["Country"], "SumOf16": sum_series.round(4)})
        .sort_values("SumOf16", ascending=False)
        .head(5),
        use_container_width=True
    )
    if (sum_series > 1.2).any() or (sum_series < 0.8).any():
        st.warning("⚠️ 일부 국가는 16유형 합이 1과 다를 수 있습니다(원 데이터 특성/추정치일 수 있음).")

st.subheader("유형별 상위 10개 국가")
if not selected_types:
    st.info("사이드바에서 MBTI 유형을 1개 이상 선택하세요.")
else:
    tabs = st.tabs(selected_types)
    for t, tab in zip(selected_types, tabs):
        with tab:
            st.altair_chart(top10_chart(df, t), use_container_width=True)

with st.expander("전체 16유형 한 번에 보기", expanded=False):
    all_tabs = st.tabs(mbti_cols)
    for t, tab in zip(mbti_cols, all_tabs):
        with tab:
            st.altair_chart(top10_chart(df, t), use_container_width=True)
