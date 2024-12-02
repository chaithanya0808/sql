SELECT
    case_id,
    case_party_details->>'party_name' AS source_party_name,  -- Value from case_party_details
    case_party_fc_profile->>'party_name' AS target_party_name, -- Current value in case_party_fc_profile
    jsonb_set(                                                -- Simulated update
        COALESCE(case_party_fc_profile, '{}'),
        '{party_name}',
        case_party_details->'party_name',
        true
    ) AS updated_case_party_fc_profile -- Simulated result after update
FROM fcem_data.fc_case_party_relationship
WHERE case_party_details ? 'party_name'  -- Only rows where party_name exists in case_party_details
LIMIT 100; -- Limit rows for testing
