from cleaning_tools import cleaning_null, data_treatment

def main():
    for i in range(1, 5):
        path = f"202{i}_LoL_esports_match_data_from_OraclesElixir.csv"
        new_cv_path = f"cleaned_data{i}.csv"
        data_treatment(path, new_cv_path)
        cleaning_null(new_cv_path, new_cv_path)
        
if __name__ == "__main__":
    main()