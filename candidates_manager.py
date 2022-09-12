import json, pprint


class CandidatesManager:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"Candidatemanaget({self.path})"

    def load_candidates_from_json(self):
        """Get data form json file"""
        with open(self.path) as file:
            data = json.load(file)
        return data

    def get_candidate_by_id(self, cid):
        """Get candidate by id"""
        candidates = self.load_candidates_from_json()
        for candidate in candidates:
            if candidate["id"] == cid:
                return candidate

    def get_candidate_by_name(self, name):
        """Get candidates by name"""
        candidates = self.load_candidates_from_json()
        name = name.lower()
        matching_candidates = [candidate for candidate in candidates if name in candidate["name"].lower()]
        return matching_candidates

    def get_candidate_by_skill(self, skill):
        """Get candidates by skill"""
        candidates = self.load_candidates_from_json()
        skill = skill.lower()
        matching_candidates = []

        for candidate in candidates:
            candidate_skills = candidate["skills"].lower().split(", ")
            if skill in candidate_skills:
                matching_candidates.append(candidate)
        return matching_candidates

    def get_all_candidates(self):
        """Get all candidates"""
        candidates = self.load_candidates_from_json()
        return candidates