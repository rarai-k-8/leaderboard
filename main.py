import csv

# CSVファイルのパス
csv_file = "leaderboard.csv"

# ユーザー名がCSVファイルに存在するか確認
def check_user_exists(username):
    try:
        df = pd.read_csv(csv_file)
        return username in df['Username'].values
    except FileNotFoundError:
        return False

# CSVファイルに新しいスコアを追加または更新
def update_score(username, score):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Username", "Score"])
    
    if username in df['Username'].values:
        df.loc[df['Username'] == username, 'Score'] = score
    else:
        df = df.append({"Username": username, "Score": score}, ignore_index=True)
    
    df.to_csv(csv_file, index=False)

if authentication_status:
    st.subheader("Update Score")
    user_score = st.number_input("Enter your score", min_value=0, value=0, step=1)
    
    if st.button("Update Score"):
        if not check_user_exists(username):
            update_score(username, user_score)
            st.success("Score updated successfully!")
        else:
            st.error("Username already exists. Score cannot be updated.")

    # スコアボードの表示
    if st.checkbox("Show leaderboard"):
        try:
            df = pd.read_csv(csv_file)
            st.write(df)
        except FileNotFoundError:
            st.error("Leaderboard is empty.")

