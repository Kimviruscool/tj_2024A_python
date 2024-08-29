from app import app
from service import *
    # 4. app.run 코드 위에 HTTP 매핑 주소 정의 controller
@app.route("/getjobinfo" , methods=['get']) # http://localhost:5000/qooqoo
def getJob():
    result = []
    getJobInfo(result)
    list2d_to_csv(result, 'jobInfo', ['회사명', '공고명', '기타'])  # 매장정보를 csv로 저장 서비스 호출
    result2 = read_csv_to_json('jobInfo')
    # print(result2)
    return result2

@app.route("/totalJob" , methods=['get']) # http://localhost:5000/qooqoo
def totalJob():
    result2 = read_csv_to_json('jobInfo')
    result = totalJobInfo(result2)
    # print(result)
    return result

@app.route("/newhistory" , methods=['get']) # http://localhost:5000/qooqoo
def newhist():
    result2 = read_csv_to_json('jobInfo')
    result = newhistory(result2)
    # print(result)
    return result
