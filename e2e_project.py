import pandas as pd
import pytest

# to check if there are any duplicate records in target
def test_duplicate_record():
    target_df = pd.read_csv("target.csv")
    duplicated_df = target_df.duplicated().sum()
    assert duplicated_df == 0, "given record has the duplicated records"

# to check weather target is blank

def test_target_blank():
    target_df = pd.read_csv("target.csv")
    assert not target_df.empty,"target is empty - please varify the tarnsformationss"

# check depto is mandatory

def test_check_dept():
    target_df = pd.read_csv("target.csv")
    dept_df = target_df['deptno'].isnull().any()
    assert dept_df == False ,"dept having null values"

# check empno has primary keys

def test_eno_uniquevalue():
    target_df = pd.read_csv("target.csv")
    countt = len(target_df['eno'].unique())
    total_count = target_df['eno'].count()
    assert total_count==countt,"record has duplicate eno"


