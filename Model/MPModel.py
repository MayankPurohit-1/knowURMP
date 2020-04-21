from database import mp_data, scroll_data
from flask import make_response, render_template, url_for, request


class MPModel:
    def list_mp(self, state, constituency):
        result = mp_data.find_one({
            "State": state,
            "Constituency": constituency
        })
        if result:
            result['_id'] = str(result['_id'])
            return make_response(render_template('profile.html', data=result))

    # def find_mp_by_constituency(self, seat):
    #     result = ConnectionModel.connect('mpdata').find_one({"Constituency": seat})
    #     if result:
    #         return make_response(render_template('profile.html', data=result))

    def home(self):
        result = scroll_data.find()
        data = {
            "result": result,
        }
        return make_response(render_template('index.html', data=data))
