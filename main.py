from flask import Flask, render_template
from candidates_manager import CandidatesManager

app = Flask(__name__)

manager = CandidatesManager("candidates.json")

@app.route('/')
def page_index():
    canddidates = manager.get_all_candidates()
    return render_template('list.html', candidates=canddidates)


@app.route('/candidate/<int:can_id>')
def page_single_candidate(can_id):
    candidate = manager.get_candidate_by_id(can_id)
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def page_search_for_candidate(candidate_name):
    candidates = manager.get_candidate_by_name(candidate_name)
    candidates_len = len(candidates)
    return render_template("search.html", candidates=candidates, candidates_len=candidates_len)

@app.route('/skill/<skill_name>')
def page_search_by_skill(skill_name):
    candidates = manager.get_candidate_by_skill(skill_name)
    candidates_len = len(candidates)
    return render_template("list_by_skills.html", candidates=candidates,
                           candidates_len=candidates_len,
                           skill_name=skill_name)



if __name__ == '__main__':
    app.run(debug=True)

